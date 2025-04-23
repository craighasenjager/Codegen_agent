# langgraph_codegen_agent/main.py

import os
import logging
from typing import TypedDict, List, Annotated, Dict, Any
import uuid

from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure script output directory exists
os.makedirs("generated_scripts", exist_ok=True)
def clean_code_output(text: str) -> str:
    """
    Cleans up LLM output by removing markdown-style code fences.
    """
    lines = text.strip().splitlines()

    # Remove starting ```python or '''python
    if lines and (lines[0].strip().startswith("```") or lines[0].strip().startswith("'''")):
        lines = lines[1:]

    # Remove ending ``` or '''
    if lines and (lines[-1].strip() in ("```", "'''")):
        lines = lines[:-1]

    return "\n".join(lines).strip()


# --- TOOL DEFINITION ---

@tool
def python_code_creator(request: str) -> str:
    """
    Generate a Python script from user request, save it to disk, and return the path.
    
    Args:
        request: A description of the Python script to generate
        
    Returns:
        The file path where the generated script was saved
    """
    logger.info(f"[python_code_creator] User request: {request}")
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # Prompt for code generation
    prompt = (
        f"Generate a Python script that {request}.\n"
        "The code must include error handling, use functions, and have comments.\n"
        "Avoid hardcoding unless explicitly requested.\n"
        "Return ONLY the code, no explanations."
    )

    response = llm.invoke(prompt)
    code = clean_code_output(response.content)

    # Save the script
    safe_name = "_".join(request.lower().split())[:50]
    filepath = f"generated_scripts/{safe_name}.py"
    with open(filepath, "w") as f:
        f.write(code)

    logger.info(f"[python_code_creator] Saved to: {filepath}")
    return f"Code saved to {filepath}"


# --- STATE SCHEMA DEFINITION ---

class CodeGenState(TypedDict):
    """State for the code generation agent."""
    messages: List[BaseMessage]


# --- AGENT SETUP ---

def create_agent():
    """Create and configure the React agent."""
    agent_llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    system_message = """
You are a Python code generation assistant that can maintain context across multiple interactions.

You can:
- Generate complete Python scripts from natural language requests
- Answer technical questions about Python and software development
- Help improve, debug, and refactor code
- Give short summaries or explanations of Python libraries and concepts
- Generate any file of any type to the user's specifications

When a user asks for code generation:
- You MUST use the available tool `python_code_creator` to create and save the script
- Do not return code directly — always call the tool to ensure the code is saved to a file
- Avoid writing the code inline unless the user is asking for help understanding a concept

When writing code:
- Always prioritise clean, production-level structure
- Use error handling, helpful comments, and modular functions
- Avoid hardcoded values unless explicitly requested
- Always ensure the code is fully functional and can be run by the user
- Return only the code from the tool — no explanations or Markdown formatting like triple backticks

Ask clarifying questions when user input is ambiguous.
Stay helpful, collaborative, and focused on quality software engineering.
"""

    
    react_agent = create_react_agent(
        agent_llm,
        tools=[python_code_creator],
        prompt=system_message
    )
    
    return react_agent


# --- GRAPH SETUP ---

def build_graph():
    """Build and return the agent graph."""
    # Create the agent
    react_agent = create_agent()
    
    # Define the agent execution step
    def run_agent_step(state: CodeGenState) -> Dict[str, Any]:
        """Execute a single step of the agent."""
        logger.info("===== Agent Step =====")
        for i, msg in enumerate(state["messages"]):
            logger.info(f"[{i}] {msg.__class__.__name__}: {msg.content}")
        
        # Invoke the agent with the current messages
        result = react_agent.invoke({"messages": state["messages"]})
        
        # Log the agent's response
        logger.info("[Agent Output]")
        logger.info(result["messages"][-1].content)
        
        # Return the updated state with the new message
        return {"messages": result["messages"]}
    
    # Create the graph
    graph = StateGraph(CodeGenState)
    graph.add_node("agent", run_agent_step)
    graph.set_entry_point("agent")
    
    # Set the finish condition - always return to allow for multi-turn conversations
    graph.add_edge("agent", END)
    
    return graph.compile()


# --- MAIN EXECUTION ---

def main():
    """Main execution function with multi-turn conversation support."""
    # Create memory for persistence
    memory = MemorySaver()
    
    # Generate a unique thread ID for this conversation
    thread_id = str(uuid.uuid4())
    logger.info(f"Starting new conversation with thread_id: {thread_id}")
    
    # Build the graph
    graph = build_graph()
    
    # Start the conversation loop
    conversation_active = True
    current_messages = []
    
    print("\n=== Python Code Generation Assistant ===")
    print("(Type 'exit' to end the conversation)\n")
    
    while conversation_active:
        # Get user input
        if not current_messages:
            # First message
            user_prompt = input("How can I assist you today? ")

        else:
            # Follow-up messages
            user_prompt = input("\nAnything else you'd like to do with this code? (or type 'exit'): ")
        
        # Check if user wants to exit
        if user_prompt.lower() in ['exit', 'quit', 'bye']:
            print("\nThank you for using the Python Code Generation Assistant!")
            conversation_active = False
            break
        
        # Create or update the messages list
        if not current_messages:
            # First turn
            current_messages = [HumanMessage(content=user_prompt)]
        else:
            # Add the new message to existing conversation
            current_messages.append(HumanMessage(content=user_prompt))
        
        # Prepare the state
        state = {"messages": current_messages}
        
        # Invoke the graph with the current state
        result = graph.invoke(
            state,
            {"configurable": {"thread_id": thread_id}}
        )
        
        # Update the current messages for the next turn
        current_messages = result["messages"]
        
        # Display the agent's response
        print("\nAssistant:", current_messages[-1].content)


if __name__ == "__main__":
    main()

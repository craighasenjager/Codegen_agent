# 🧠 Codegen Agent (LangGraph + OpenAI)

This project is a fully conversational, ReAct-style code generation assistant powered by **LangGraph**, **OpenAI GPT-4o**, and a flexible tool system.

The assistant allows you to:
- 💬 Speak naturally with the agent: "Make me a PDF generator" or "Build a calculator"
- ⚙️ Automatically generate clean, runnable Python scripts
- 💾 Save scripts directly to a structured output folder
- 🔁 Maintain memory across interactions to support multi-turn refinement

---

## 🚀 Features

- Built with `langgraph.prebuilt.create_react_agent`
- Uses `python_code_creator` tool to generate scripts
- Cleans code output automatically (removes Markdown, quotes, etc.)
- Saves all code into `generated_scripts/`
- Tracks conversation state via `thread_id` and memory
- Configured for production-quality responses (no explanations, clean formatting)

---

## 🧰 Stack

- `langgraph`
- `langchain-core`
- `langchain-openai`
- `OpenAI GPT-4o`
- Python 3.11+

---

## 📂 Project Structure

```
/codegen_agent
├── main.py               # Entry point with CLI loop and LangGraph agent
├── generated_scripts/    # Output directory for generated .py files
├── setup.sh              # Optional installer for dependencies
├── requirements.txt      # Python dependencies
└── .gitignore            # Standard ignore rules
```

---

## 🛠 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the assistant
python main.py
```

Then start chatting:
```text
> Make me a terminal-based tic-tac-toe game
> Actually, use a 4x4 grid instead
> Save it and create a PDF summary too
```

---

## ✨ Example Output
A user can say:
> "Build a command-line calculator with error handling."

The assistant will:
- Call the `python_code_creator` tool
- Generate clean code
- Save to `generated_scripts/create_a_command_line_calculator.py`
- Return a message like: "Code saved to generated_scripts/create_a_command_line_calculator.py"

---

## 🧠 Memory & Threading
Each session uses a unique `thread_id` via `uuid.uuid4()` to persist conversation state and enable future expansion.

LangGraph `MemorySaver` keeps checkpoints for debugging or multi-turn continuation.

---

## 🔐 Security Note
The assistant **does not execute any generated code**. If you choose to run generated files, do so with caution and proper review.

---

## 📄 License
MIT — free to use, modify, and share.

---

## 👨‍💻 Author
This project was built by Dotcloud AI as a reusable LangGraph-based intelligent code generation tool.

Contributions welcome!

```python
import sys

def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

def calculate(expression):
    """Function to evaluate a simple addition or subtraction expression."""
    try:
        # Split the expression by spaces
        parts = expression.split()
        
        if len(parts) != 3:
            raise ValueError("Invalid format. Use: <number> <operator> <number>")
        
        num1, operator, num2 = parts
        
        # Convert numbers from string to float
        num1 = float(num1)
        num2 = float(num2)
        
        if operator == '+':
            return add(num1, num2)
        elif operator == '-':
            return subtract(num1, num2)
        else:
            raise ValueError("Invalid operator. Only + and - are supported.")
    
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    """Main function to run the command-line calculator."""
    if len(sys.argv) != 2:
        print("Usage: python calculator.py '<number> <operator> <number>'")
        sys.exit(1)
    
    expression = sys.argv[1]
    result = calculate(expression)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```
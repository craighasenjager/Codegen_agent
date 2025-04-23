
import sys

def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

def calculate(operation, num1, num2):
    """Function to perform calculation based on the operation."""
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    else:
        raise ValueError("Invalid operation. Only '+' and '-' are supported.")

def main():
    """Main function to handle command-line input and perform calculations."""
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <num1> <operation> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        operation = sys.argv[2]
        num2 = float(sys.argv[3])
        
        result = calculate(operation, num1, num2)
        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

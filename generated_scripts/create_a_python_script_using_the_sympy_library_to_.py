```python
from sympy import symbols, diff, sympify
from sympy.core.sympify import SympifyError

def get_user_input():
    """
    Get a mathematical function as input from the user.
    """
    return input("Enter a mathematical function in terms of x: ")

def calculate_derivative(function_str):
    """
    Calculate the derivative of the given function string.
    
    Parameters:
    function_str (str): The function as a string.
    
    Returns:
    str: The derivative of the function.
    """
    x = symbols('x')
    try:
        # Convert the string to a sympy expression
        function = sympify(function_str)
        # Calculate the derivative
        derivative = diff(function, x)
        return derivative
    except SympifyError:
        return "Invalid function input. Please enter a valid mathematical expression."

def main():
    """
    Main function to execute the script.
    """
    function_str = get_user_input()
    derivative = calculate_derivative(function_str)
    print(f"The derivative of the function is: {derivative}")

if __name__ == "__main__":
    main()
```
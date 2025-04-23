
import sympy as sp

def get_function_input():
    """
    Get the function input from the user and validate it.
    """
    try:
        func_str = input("Enter the function of x to differentiate (e.g., 'sin(x) + x**2'): ")
        x = sp.symbols('x')
        func = sp.sympify(func_str)
        return func, x
    except (sp.SympifyError, TypeError):
        raise ValueError("Invalid function input. Please enter a valid mathematical expression.")

def compute_derivative(func, x):
    """
    Compute the symbolic derivative of the function.
    """
    try:
        derivative = sp.diff(func, x)
        return derivative
    except Exception as e:
        raise RuntimeError(f"Error computing derivative: {e}")

def evaluate_derivative(derivative, x, value):
    """
    Evaluate the derivative at a specific numerical value.
    """
    try:
        numerical_value = derivative.subs(x, value)
        return numerical_value.evalf()
    except Exception as e:
        raise RuntimeError(f"Error evaluating derivative: {e}")

def main():
    """
    Main function to run the advanced calculator.
    """
    try:
        func, x = get_function_input()
        derivative = compute_derivative(func, x)
        print(f"The derivative of the function is: {derivative}")

        while True:
            try:
                value = float(input("Enter a numerical value to evaluate the derivative (or 'q' to quit): "))
                result = evaluate_derivative(derivative, x, value)
                print(f"The derivative evaluated at x = {value} is: {result}")
            except ValueError:
                print("Exiting the evaluation loop.")
                break
            except RuntimeError as e:
                print(e)

    except ValueError as ve:
        print(ve)
    except RuntimeError as re:
        print(re)

if __name__ == "__main__":
    main()

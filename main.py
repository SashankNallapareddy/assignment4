"""
The main class
"""
import sys
from decimal import Decimal, InvalidOperation
from calculator.operation import Operation


def calculate_and_print(a, b, operation_name):
    """
    Perform calculations from user input
    """
    operation_instance = Operation()  # Create an instance of the Operation class
    operation_mappings = {
        'add': operation_instance.add,
        'subtract': operation_instance.subtract,
        'multiply': operation_instance.multiply,
        'divide': operation_instance.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            # pylint: disable=line-too-long
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    # pylint: disable=broad-exception-caught
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    """
    Perform calculations from user input
    """
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    _, a, b, operater = sys.argv
    calculate_and_print(a, b, operater)

if __name__ == '__main__':
    main()

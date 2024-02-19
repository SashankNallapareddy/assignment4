"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""
import pytest
from calculator.calculation import calculation
from calculator.operation import Operation

def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    calc = calculation(a, b, operation)
    assert calc.compute() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically
    undefined and should be handled as an error.
    """
    operation_instance = Operation()
    calc = calculation(10, 0, operation_instance.divide)
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        calc.compute()

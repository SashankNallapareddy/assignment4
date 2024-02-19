"""
Operation test methods
"""
import pytest
from calculator.calculation import calculation
from calculator.operation import Operation


def test_operation(a, b, operation, expected):
    '''Testing various operations'''
    calculator = calculation(a, b, operation)
    assert calculator.compute() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    operation_instanc = Operation()
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        calculator = calculation(10, 0, operation_instanc.divide)
        calculator.compute()

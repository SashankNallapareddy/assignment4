"""
Module docstring: A brief description of the test module.
"""

from calculator.operation import Operation
from calculator.calculation import calculation

def test_addition():
    """
    Test addition operation.
    """
    calculate = calculation(2, 3, Operation.add)
    result = calculate.compute()
    assert result == 5

def test_subtraction():
    """
    Test subtraction operation.
    """
    calculate = calculation(2, 2, Operation.subtract)
    result = calculate.compute()
    assert result == 0

def test_division():
    """
    Test division operation.
    """
    try:
        calculate = calculation(2, 0, Operation.divide)
        result = calculate.compute()
        assert result == 0
    except ZeroDivisionError as e:
        assert str(e) == "division by zero"

def test_multiply():
    """
    Test multiplication operation.
    """
    calculate = calculation(2, 2, Operation.multiply)
    result = calculate.compute()
    assert result == 4

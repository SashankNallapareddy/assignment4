'''My Calculator Test'''

# Correct the import order by placing standard library imports before third-party library imports,
# adhering to PEP 8 guidelines for import ordering.
from decimal import Decimal
import pytest

from calculator.calculation import calculation
from calculator.calculation_history import CalculationsHistory
from calculator.operation import Operation


# pytest.fixture is a decorator that marks a function as a fixture,
# a setup mechanism used by pytest to initialize a test environment.
# Here, it's used to define a fixture that prepares the test environment for calculations tests.
@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    # Clear any existing calculation history to ensure a clean state for each test.
    CalculationsHistory.clear_history()
    # Add sample calculations to the history to set up a known state for testing.
    # These calculations represent typical use cases and allow tests to verify that
    # the history functionality is working as expected.
    operation_instance = Operation()
    CalculationsHistory.add_history(calculation(10, 5, operation_instance.add))
    CalculationsHistory.add_history(calculation(20, 3, operation_instance.subtract))

# def test_add_calculation(setup_calculations):
#     """Test adding a calculation to the history."""
#     # Create a new Calculation object to add to the history.
#     operation_instance = Operation()
#     calc = calculation(2, 2, operation_instance.add)
#     # Add the calculation to the history.
#     CalculationsHistory.add_history(calc)
#     # Assert that the calculation was added to the history by checking
#     # if the latest calculation in the history matches the one we added.

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    # Retrieve the calculation history.
    history = CalculationsHistory.get_history()
    # Assert that the history contains exactly 2 calculations,
    # which matches our setup in the setup_calculations fixture.
    assert len(history) == 2

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    # Clear the calculation history.
    CalculationsHistory.clear_history()
    # Assert that the history is empty by checking its length.
    assert len(CalculationsHistory.get_history()) == 0

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    # Retrieve the latest calculation from the history.
    latest = CalculationsHistory.get_latest()
    # Assert that the latest calculation matches the expected values,
    # specifically the operands and operation used in the last added calculation
    # in the setup_calculations fixture.
    assert latest.a == Decimal('20') and latest.b == Decimal('3')

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
def test_find_by_operation(setup_calculations):
    """Test finding calculations in the history by operation type."""
    # Find all calculations with the 'add' operation.
    add_operations = CalculationsHistory.find_by_operation("add")
    # Assert that exactly one calculation with the 'add' operation was found.
    assert len(add_operations) == 1
    # Find all calculations with the 'subtract' operation.
    subtract_operations = CalculationsHistory.find_by_operation("subtract")
    # Assert that exactly one calculation with the 'subtract' operation was found.
    assert len(subtract_operations) == 1

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    # Ensure the history is empty by clearing it.
    CalculationsHistory.clear_history()
    # Assert that the latest calculation is None since the history is empty.
    assert CalculationsHistory.get_latest() is None

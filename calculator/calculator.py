"""
Calculator class is used to calculate the values and add the result to store history
"""

from calculator.operation import Operation
from calculator.calculation_history import CalculationsHistory
from calculator.calculation import calculation

class Calculator:
    """
    Calculates and stores the results in history
    """

    def __init__(self):
        """
        Initializes a new Calculator instance.
        """
        self.operation_instance = Operation()

    def perform_calculation(self, a, b, operation_func):
        """
        Perform a calculation using the specified operation.

        Args:
            a (float): The first operand.
            b (float): The second operand.
            operation_func (callable): The operation to perform.

        Returns:
            float: The result of the computation.
        """
        calculate = calculation(a, b, operation_func)
        result = calculate.compute()
        CalculationsHistory.add_history(calculate)
        return result

    def get_calculation_history(self):
        """
        Get the history of calculations.

        Returns:
            list: List of calculations in the history.
        """
        return CalculationsHistory.get_history()

"""
Module used to get calculation history.
"""
from typing import List
from calculator.calculation import calculation


class CalculationsHistory:
    """
    Get Calculation history.
    """
    history = []

    @classmethod
    def add_history(cls, calculator):
        """
        Add a calculation to the history.

        Args:
            calculation: The calculation to be added.
        """
        cls.history.append(calculator)

    @classmethod
    def get_history(cls):
        """
        Get the history of calculations.

        Returns:
            list: List of calculations in the history.
        """
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[calculation]:
        """Find and return a list of calculations by operation name."""
        return [calc for calc in cls.history if calc.operate.__name__ == operation_name]
    
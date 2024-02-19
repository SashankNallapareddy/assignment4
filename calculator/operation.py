"""
Operation is used to add , subtract, divide and multiply given two numbers
"""

class Operation:
    """
    Class takes on 4 methods for performing different operations and returns the result
    """

    @staticmethod
    def add(a, b):
        """
        Adds two numbers.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the addition.
        """
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Subtracts two numbers.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the subtraction.
        """
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Multiplies two numbers.

        Args:
            a (float): The first operand.
            b (float): The second operand.

        Returns:
            float: The result of the multiplication.
        """
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divides two numbers.

        Args:
            a (float): The numerator.
            b (float): The denominator.

        Returns:
            float: The result of the division.

        Raises:
            ZeroDivisionError: If the denominator is zero.
        """
        try:
            result = a / b
            return result
        # pylint: disable=try-except-raise
        except ZeroDivisionError:
            raise

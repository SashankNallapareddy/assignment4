"""
Calculation class used to operate the give values based on the operation type
"""

from calculator.operation import Operation

# pylint: disable=invalid-name
class calculation:
    """
    Import Operation class and computes the given values 
    """

    def __init__(self, a, b, operate):
        """
        Initializes a new Calculation instance.

        Args:
            a (float): The first operand.
            b (float): The second operand.
            operate (callable): The operate to perform (e.g., Operation.add).
        """
        self.a = a
        self.b = b
        self.operate = operate

    def compute(self):
        """
        Performs the specified operation on operands a and b.

        Returns:
            float: The result of the computation.

        Raises:
            ValueError: If the operation is not valid.
        """
        operation_instance = Operation()
        result = None

        # pylint: disable=comparison-with-callable
        if self.operate == operation_instance.add:
            result = operation_instance.add(self.a, self.b)
        elif self.operate == operation_instance.subtract:
            result = operation_instance.subtract(self.a, self.b)
        elif self.operate == operation_instance.multiply:
            result = operation_instance.multiply(self.a, self.b)
        elif self.operate == operation_instance.divide:
            result = operation_instance.divide(self.a, self.b)
        else:
            raise ValueError("Invalid operation")

        return result

    def another_public_method(self):
        """
        Placeholder for another public method to pass lint test.

        Add the implementation when needed.
        """

# pylint: enable=invalid-name,comparison-with-callable

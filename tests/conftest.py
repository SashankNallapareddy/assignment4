"""
Conftest class
"""
# conftest.py
from decimal import Decimal
from faker import Faker
from calculator.operation import Operation

fake = Faker()

def generate_test_data(num_records):
    """
    Method to generate test data
    """
    # Define operation mappings for both Calculator and Calculation tests
    operation_instance = Operation()  # Create an instance of the Operation class
    operation_mappings = {
        'add': operation_instance.add,
        'subtract': operation_instance.subtract,
        'multiply': operation_instance.multiply,
        'divide': operation_instance.divide
    }
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        # pylint: disable=line-too-long
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # pylint: disable=comparison-with-callable
        if operation_func == operation_instance.divide:
            # pylint: disable=comparison-with-callable
            b = Decimal('1') if b == Decimal('0') else b
        try:
            if operation_func == operation_instance.divide and b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """
    Method to generate test records number from user 
    """
    # pylint: disable=line-too-long
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Method to generate tests
    """
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        # pylint: disable=line-too-long
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a,b,operation,expected", modified_parameters)

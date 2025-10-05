from smolagents import tool
import math

@tool
def Add(numbers: list[int]) -> int:
    """
    Add a list of numbers and return the sum.
    Args:
        numbers (list[int]): A list of numbers to add.
    """
    return sum(numbers)

@tool
def Multiply(numbers: list[int]) -> int:
    """
    Multiply a list of numbers and return the product.
    Args:
        numbers (list[int]): A list of numbers to multiply.
    """
    return math.prod(numbers)
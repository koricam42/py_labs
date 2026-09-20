"""
Program name: Geometry Calculator - rectangle.py
Author: Jordan Mensah
Purpose: Calculate the area and perimeter of a rectangle
Starter code: N/A
Date: 9/17/26
"""


def calc_area(width: float, height: float) -> float:
    """Calculates the area of a rectangle

    Args:
        width (float): The width of a rectangle
        height (float): The height of a rectangle

    Returns:
        float: The area of a rectangle
    """
    area = width * height
    return area

def calc_perimeter(width: float, height: float) -> float:
    """Calculates the perimeter of a rectangle

    Args:
        width (float): The width of a rectangle
        height (float): The height of a rectangle

    Returns:
        float: The perimeter of a rectangle
    """
    perimeter = 2 * (height + width)
    
    return perimeter
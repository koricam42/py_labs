"""
Program name: Geometry Calculator - circle.py
Author: Jordan Mensah
Purpose: Calculate the area and circumference of a circle
Starter Code (References):
    - Type Hints: https://www.geeksforgeeks.org/python/type-hints-in-python/
    - Area Formula: https://www.wikihow.com/Calculate-the-Area-of-a-Circle
    - Circumference Formula: https://www.wikihow.com/Calculate-the-Circumference-of-a-Circle
Date: 9/17/26
"""

import math

def calc_area(radius: float) -> float:
    """Calculates the area of a circle

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The calculated area of the circle
    """
    area = math.pi * radius ** 2
    return area

def calc_circumference(radius: float) -> float:
    """Calculates the circumference of a circle
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The calculated circumference of the circle
    """                                                                                                                                                                    
    circumference = 2 * math.pi * radius
    return circumference
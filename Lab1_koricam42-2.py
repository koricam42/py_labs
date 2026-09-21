"""
Program name: Geometry Calculator - main
Author: Jordan Mensah
Purpose: This program calculates area and perimeter or circumference of a rectangles and circles via imported functions.
Starter Code (References):
    - Overall Program Structure (CH1-11): https://learning.oreilly.com/library/view/python-crash-course/9781098156664/
    - Type Hints: https://www.geeksforgeeks.org/python/type-hints-in-python/
    - Exception Handling: https://www.geeksforgeeks.org/python/python-exception-handling/
    - Output Formatting/Project Guidelines: https://courses.cscc.edu/ultra/courses/_238744_1/assessment/_28741586_1/attempt/create?courseId=_238744_1 
Date: 9/17/26
"""

# Aliases Import Explanation 
# Both imports have a function named calc_area, so to avoid naming conflicts,
# I utilized aliases to differentiate the two imported functions.

from rectangle import calc_area as rectangle_area, calc_perimeter
from circle import calc_area as circle_area, calc_circumference

def error_handler(user_text: str) -> float:
    """Function to safely handle invalid user input to prevent crashing.

    Args:
        user_text (str): Text to prompt user for input.

    Returns:
        float: valid decimal number input from the user.
    """
    while True:
        try:
            true_input = float(input(user_text))

            if true_input <= 0:
                print("Invalid input. Please enter a number greater than 0")
                continue

            return true_input
        except ValueError:
            print("Invalid input. Please enter a number.")

# I modeled the print statements to match the output of the examples in the lab instuctions
# But I'm not sure if the print output formatting (of the non-math sections) has to match the example perfectly
def main() -> None:
    """Runs main menu loop for program, handles user inputs to calculate and display measurements"""
    # Could potentially improve the looks of the main menu with ASCII art
    while True:
        print("\nGeometry Calculator")
        print("-------------------")
        print("1. Calculate Circle Area")
        print("2. Calculate Circle Circumference")
        print("3. Calculate Rectangle Area")
        print("4. Calculate Rectangle Perimeter")
        print("5. Exit")     

        user_input = input("Select an option (1-5): ")
        # Could potentially shorten this by merging the 4 options into 2,
        if user_input == "1":
            radius = error_handler("Enter the radius of the circle: ")
            area = circle_area(radius)
            print(f'\nThe area of the circle is: {area}')
            input("Press Enter to continue.")
        elif user_input == "2":
            radius = error_handler("Enter the radius of the circle: ")
            circumference = calc_circumference(radius)
            print(f'\nThe circumference of the circle is: {circumference}')
            input("Press Enter to continue.")
        elif user_input == "3":
            width = error_handler("Enter the width of the rectangle: ")
            height = error_handler("Enter the height of the rectangle: ")
            area = rectangle_area(width, height)
            print (f'\nThe area of the rectangle is: {area}')
            input("Press Enter to continue.")
        elif user_input == "4":
            width = error_handler("Enter the width of the rectangle: ")
            height = error_handler("Enter the height of the rectangle: ")
            perimeter = calc_perimeter(width, height)
            print (f'\nThe perimeter of the rectangle is: {perimeter}')
            input("Press Enter to continue.")
        elif user_input == "5":
            print("\nGoodbye.")
            break
        else:
            print("Invalid input. Options are only 1-5. Please try again.:")

main()

"""
Program name: Geometry Calculator - main
Author: Jordan Mensah
Purpose: This program calculates area and perimeter or circumference of a rectangles and circles via imported functions.
Starter code: N/A
Date: 9/17/26
"""

# Aliases import explanation (TBD)

from rectangle import calc_area as rectangle_area, rectangle_perimeter
from circle import calc_area as circle_area, circle_circumference

# I modeled the print statements to match the output of the examples in the lab instuctions
# But I'm not sure if the print output (of the non-math sections) has to match the example perfectly
def main():
    while True:
        print("Geometry Calculator")
        print("-------------------")
        print("1. Calculate Circle Area")
        print("2. Calculate Circle Circumference")
        print("3. Calculate Rectangle Area")
        print("4. Calculate Rectangle Perimeter")
        print("5. Exit")     

        user_input = input("Select and option (1-5): ")

# Placeholders for 1-4
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid input. Options are only 1-5. Please try again.:")

main()

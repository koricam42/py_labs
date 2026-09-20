"""
Program name: Geometry Calculator - main
Author: Jordan Mensah
Purpose: This program calculates area and perimeter or circumference of a rectangles and circles via imported functions.
Starter code: N/A
Date: 9/17/26
"""

# Aliases import explanation (TBD)

from rectangle import calc_area as rectangle_area, calc_perimeter
from circle import calc_area as circle_area, calc_circumference

# I modeled the print statements to match the output of the examples in the lab instuctions
# But I'm not sure if the print output (of the non-math sections) has to match the example perfectly
def main():
    while True:
        print("\nGeometry Calculator")
        print("-------------------")
        print("1. Calculate Circle Area")
        print("2. Calculate Circle Circumference")
        print("3. Calculate Rectangle Area")
        print("4. Calculate Rectangle Perimeter")
        print("5. Exit")     

        user_input = input("Select an option (1-5): ")

        if user_input == "1":
            radius = float(input("Enter the radius of the circle: "))
            area = circle_area(radius)
            print(f'\nThe area of the circle is: {area}')
        elif user_input == "2":
            radius = float(input("Enter the radius of the circle: "))
            circumference = calc_circumference(radius)
            print(f'\nThe circumference of the circle is: {circumference}')
        elif user_input == "3":
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            area = rectangle_area(width, height)
            print (f'\nThe area of the rectangle is: {area}')
        elif user_input == "4":
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            perimeter = calc_perimeter(width, height)
            print (f'The perimeter of the rectangle is: {perimeter}')
        elif user_input == "5":
            print("\nGoodbye.")
            break
        else:
            print("Invalid input. Options are only 1-5. Please try again.:")

main()

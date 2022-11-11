'''
Write a piece of code that prompts the user for the area of a square (in cm2). The code then displays the side of the square (in cm).
'''
import math
square_area = float(
    input("What's the size of the square (in square centimetres)?: "))
side_of_square = math.sqrt(square_area)
print(f"Each side of the square is {side_of_square}cm")

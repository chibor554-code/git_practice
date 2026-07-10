# creating functions to do different tasks

# Area of a circle

import math
def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area

def perimeter_rectangle(length, width):
    perimeter = 2 * (length + width)
    return perimeter

def is_palindrome(word):
    return word == word[::-1]


# print(f"Area of circle: {area_of_circle(7):.2f}")
# print(f"Rectangle perimeter: {rectangle_perimeter(10, 5)}")
# print(is_palindrome("madam"))
# print(is_palindrome("python"))

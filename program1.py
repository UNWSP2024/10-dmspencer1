# Title: Triangle
# Author: Dalila Spencer
# Date: 2025-11-6

# From "Object-oriented Programming (OOP) in Python (Easy to Understand Guide) #20"
# From Programiz on YouTube

# Create a class named Triangle

# Create an object from it.
# The object will have three attributes named a, b, and c that represent the sides of the triangle.

# The Triangle class will have two methods:
# the init method to initialize the sides
# a method to calculate the perimeter of the triangle from its sides

# The perimeter of the triangle should be printed from outside the class.

class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    def set_c(self, c):
        self.__c = c

    def calc_perimeter(self):
        perimeter = self.__a + self.__b + self.__c

        return perimeter

side_a = float(input('What is the length of the first side?: '))
side_b = float(input('What is the length of the second side?: '))
side_c = float(input('What is the length of the third side?: '))

triangle = Triangle(side_a, side_b, side_c)

print(f'The perimeter of the triangle is {triangle.calc_perimeter():.2f}')
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(0, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 0
my_rectangle.height = 9
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

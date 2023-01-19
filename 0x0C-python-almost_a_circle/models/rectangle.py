#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base:
        In the file models/rectangle.py
        Class Rectangle inherits from Base
        Private instance attributes, each with its own
        public getter and setter:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
        Class constructor:
        def __init__(self, width, height, x=0, y=0, id=None):
        Call the super class with id - this super call
        with use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute"""


import json


class Base:
    """The parent class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """The first child class from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The initialization of the rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """The area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """The method to display in #"""
        for i in range(self.__height):
            print('#' * self.__width)
        for i in range(self.__y):
            print('#' * self.__x)

    def update(self, *args, **kwargs):
        """The method for assigning an argument to each attribute"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """The method to print a string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self):
        """The method to convert to dictionary"""
        return {
            'y': self.__y,
            'x': self.__x,
            'id': self.id,
            'width': self.__width,
            'height': self.__height
            }

    @classmethod
    def save_to_file(cls, list_objs):
        """The class method"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = json.dumps(list_dictionaries)
        with open(filename, 'w') as f:
            f.write(json_string)

    @property
    def width(self):
        """The getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for width"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """The getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for height"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """The getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for x"""
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """The getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter for y"""
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")

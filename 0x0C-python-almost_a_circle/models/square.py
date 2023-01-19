#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle:\
        In the file models/square.py
        Class Square inherits from Rectangle
        Class constructor: def __init__(self, size, x=0, y=0, id=None)::
        Call the super class with id, x, y, width and height -
        this super call will use the logic of the __init__ of the
        Rectangle class. The width and
        height must be assigned to the value of size
        You must not create new attributes for this class,
        use all attributes of Rectangle - As reminder:
        a Square is a Rectangle with the same width and height
        All width, height, x and y validation must inherit from Rectangle
        - same behavior in case of wrong data
        The overloading __str__ method should return-
        [Square] (<id>) <x>/<y> - <size> - in our case, width or height"""


class Base:
    """The main parent class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """The first child clas from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """The initialization"""
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
            self.id = args[0]
        elif len(args) > 1:
            self.__width = args[1]
        elif len(args) > 2:
            self.__height = args[2]
        elif len(args) > 3:
            self.__x = args[3]
        elif len(args) > 4:
            self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """The method to print a string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format\
                (self.id, self,__x, self,__y, self,__width, self.__height)

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


class Square(Rectangle):
    """The class Square that inherits from its parent class"""
    def __init__(self, size, x=0, y=0, id=None):
        """The initialization of the components"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The method to print a string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """The getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """The setter for size"""
        self.width = value
        self.height = value

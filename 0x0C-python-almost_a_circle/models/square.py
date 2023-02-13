#!/usr/bin/python3
"""Defines a class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square
        Args:
            size (int):size of the new Square
            x(int): x coordinate of the new Square
            y(int): y coordinate of the new Square
            id(int): identity of the new Square
        """
        self.size = size
        self.x = x
        self.y = y

        super().__init__(size, size, x, y, id)

    @property
    def size (self):
        """Gets the size of the Square"""
        return self.width

    @size.setter
    def size (self, value):
        self.width = value
        self.height = value

    def update (self, *args, **kwargs)):
        """Updates the Square
        Args:
            *args (ints): New values for attributes
                1st argument represents the id attribute
                2nd argument represents the size attribute
                3rd argumentrepresents the x attribute
                4th argument represents the y attribute
            **kwargs (dict): New key/value pairs of attributes
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a +=1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items:
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {
                "id": self.id,
                "width": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Return the print() and str() representation of the Square"""
        return "[Square] ([]) {}/{}".format(self.id, self.x,
                                               self.y, self.width)

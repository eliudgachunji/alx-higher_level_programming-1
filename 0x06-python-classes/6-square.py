#!/usr/bin/python3
"""Defining a class called Square"""


class Square:
    """
    class Square definition
    Args:
        size (int): size of a side in square
    Functions:
        __init__(self, size, position)
        size(self)
        size(self, value)
        position(self)
        position(self, value)        
        area(self)
        my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes square"""
        self.size = size

    @property
    def size(self):
        """"Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: sets size to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            
           @property
    def position(self):
        """"Gets the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position to tuple if value is tuple of 2 positive integers"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates area of square"""
        return (self.__size)**2

    def my_print(self):
       if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))

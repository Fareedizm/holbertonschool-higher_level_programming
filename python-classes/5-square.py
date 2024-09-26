#!/usr/bin/python3
"""Module that defines a Square class with printing capability."""

class Square:
    """A class that defines a square with a private attribute size."""

    def __init__(self, size=0):
        """Initializes the square with a given size."""
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the '#' character."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print('#' * self.__size)


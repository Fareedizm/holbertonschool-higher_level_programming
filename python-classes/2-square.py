#!/usr/bin/python3
"""Module that defines a Square class with size validation."""

class Square:
    """A class that defines a square with a private attribute size."""

    def __init__(self, size=0):
        """Initializes the square with a given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

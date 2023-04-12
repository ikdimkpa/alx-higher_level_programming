#!/usr/bin/python3
"""Defines a subclass Square of a class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a new square.
        Args:
            size (int): The size of the new square.
        """
        self().integer_validator("size", size)
        super().__init__(self, size)
        self.__size = size

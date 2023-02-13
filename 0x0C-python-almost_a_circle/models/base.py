#!/usr/bin/python3

"""Defining a base model class"""
import json


class Base:
    """Represents the base model for all classes
    __nb_objects: the number of instantied Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base
        Args:
            id: the identity of the new Base(int)
        """
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


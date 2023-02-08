#!/usr/bin/python3
"""Defines a function that writes a string"""


def write_file(filename="", taxt=""):
    """write a string to UTF8"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

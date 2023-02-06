#!/usr/bin/python3
""" Creating Mylist class that inherits from list"""

class MyList(list):
    def print_sorted(self):
        """
        Prints the list in sorted order
        """
        print(sorted(self))

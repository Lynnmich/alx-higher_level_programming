#!/usr/bin/python3

"""a function that reads a text file (UTF8) and prints it to stdout"""

def read_file(filename=""):

    with open("UTF8", encoding="utf-8") as f:
        print(UTF8.read(), end"")

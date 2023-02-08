Input/Output
The with function guarantees that the file will close if the program crashes
open allows you to open your file and mode 'w' will overwite anything inside the file.
the mode will automatically default to read if you do not define it.

JSON Module
It always produces string objects and not byte objects therefore; fp.write must support str input.
To load data into python as a string use:
json.loads()
for an object:
json.load()

To write a file in json use json.dump method
for data to be converted to a json file:
json.dump()
to a string:
json.dumps()

Prototypes:
def read_file(filename=""):

Prototype: def write_file(filename="", text=""):

def append_write(filename="", text=""):

def to_json_string(my_obj):

def from_json_string(my_str):

def save_to_json_file(my_obj, filename):

def load_from_json_file(filename):

Function - save_to_json_file from 5-save_to_json_file.py
and        load_from_json_file from 6-load_from_json_file.py

def class_to_json(obj):

def to_json(self):

def to_json(self, attrs=None):

def to_json(self, attrs=None):
def reload_from_json(self, json):

def pascal_triangle(n):


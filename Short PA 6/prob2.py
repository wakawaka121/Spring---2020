"""
File: prob2.py
Author: Derek Tominaga
Purpose: This function contains
a function to bound a value, as well
as a class Color to generate a rgb value
as string, a hex value, and a standarized
color.
Course: CSC 120, spring 2020
"""

def bound_input(value):
    if value < 0:
        return 0
    if value > 255:
        return 255
    else:
        return value
class Color:
    def __init__(self, r, g, b):
        self._r = bound_input(r)
        self._g = bound_input(g)
        self._b = bound_input(b)

    def __str__(self):
        #string = "rgb(" + str(self._r) + str(self._g) + str(self._b) + ")"
        return (f"rgb({self._r},{self._g},{self._b})")

    def html_hex_color(self):
        return (f"#{self._r:02X}{self._g:02X}{self._b:02X}")

    def get_rgb(self):
        return_tuple = (self._r, self._g, self._b)
        return return_tuple

    def set_standard_color(self, name):
        case_name = name.lower()
        assert case_name in ["red", "yellow", "white", "black"]
        if case_name == "red":
            self._r = 255
            self._g = 0
            self._b = 0
        elif case_name == "yellow":
            self._r = 255
            self._g = 255
            self._b = 0
        elif case_name == "white":
            self._r = 255
            self._g = 255
            self._b = 255
        elif case_name == "black":
            self._r = 0
            self._g = 0
            self._b = 0

    def remove_red(self):
        self._r = 0
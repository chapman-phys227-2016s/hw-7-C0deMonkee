#! /usr/bin/env python

"""
File: Polynomial_dict.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 7.28
Date: April 3, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Uses a dictionary to hold coefficients, and changes the add function so that it uses a dictionary
"""

import numpy as np

class Polynomial():
    def __init__(self, c):
        """
        c - coefficients of the polynomial, dictionary form this time
        """
        self.coeff = c
    def __add__(self, polynomial2):
        """
        adds this polynomial to another (polynomial2)
        """
        result = self.coeff
        for key in polynomial2.coeff:
            if key in self.coeff:
                result[key] = result[key] + polynomial2.coeff[key]
            else:
                result[key] = polynomial2.coeff[key]

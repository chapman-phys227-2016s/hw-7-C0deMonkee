#! /usr/bin/env python

"""
File: Polynomial_vec.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 7.27
Date: May 3, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: class implementation of a polynomial, can be differentiated
"""
import numpy as np

class Polynomial():
    def __init__(self, c):
        """
        c - coefficients of the polynomial
        """
        self.coeff = np.zeros(len(c))
        for i in xrange(len(c)):
            self.coeff[i] = c[i]
    def __add__(self, polynomial2):
        """
        adds this polynomial to another (polynomial2)
        """
        if len(self.coeff) > len(polynomial2.coeff):
            _longer = True
            length = len(polynomial2.coeff)
        else:
            _longer = False
            length = len(self.coeff)
        result_coeff = np.add(self.coeff[0:length], polynomial2.coeff[0:length])
        if _longer:
            result_coeff = np.append(result_coeff, self.coeff[length:])
        else:
            result_coeff = np.append(result_coeff, polynomial2.coeff[length:])
        return Polynomial(result_coeff)
    def __call__(self, x):
        """
        evaluates the polynomial at point x
        """
        array = numpy.zeros(len(self.coeff))
        for i in xrange(len(array)):
            array[i] = x**i
        return numpy.dot(self.coeff, array) # the vectorized part
    def differentiate(self):
        """
        differentiate this polynomial
        """
        n = len(self.coeff)
        self.coeff[:-1] = numpy.linspace(1, n-1, n-1)*self.coeff[1:]
        self.coeff = self.coeff[:-1]

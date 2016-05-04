#! /usr/bin/env python

"""
File: Lagrange_poly3.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: 7.8
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implements earlier code as a class
"""
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

class Lagrange():
    def __init__(self, f, n, xmin, xmax, axis, resolution = 1001):
        self.f = f
        self.n = n
        self.xmin = xmin
        self.xmax = xmax
        self.axis = axis
        self.resolution = resolution
    def __call__(self):
        self.graph(self.abs, 2, -2, 2, [-3,3,0,1])
        self.graph(self.abs, 4, -2, 2, [-3,3,0,1])
        self.graph(self.abs, 6, -2, 2, [-3,3,0,1])
        self.graph(self.abs, 10, -2, 2, [-3,3,0,1])
        self.graph(self.abs, 13, -2, 2, [-3,3,0,1])
        self.graph(self.abs, 20, -2, 2, [-3,3,0,1])
    def p_L(self, x, xp, yp):
        """
        Evaluates (5.21)
        """
        result = 0
        for i, elem_y in enumerate(yp):
            result += float(elem_y) * self.L_k(x, i, xp, yp)
        return result

    def L_k(self, x, k, xp, yp):
        """
        Evaluates (5.22)
        """
        product = 1.0
        for i, elem_x in enumerate(xp):
            if(i == k):
                continue
            product *= (float((x - elem_x)) / float((xp[k] - elem_x)))
        return product
    def sin(self, x):
        return np.sin(x)
    def abs(self, x):
        return np.abs(x)
    def graph(self, f, n, xmin, xmax, axis, resolution = 1001):
        """
        Plots p_L based on points taken from f(x)
        """
        x = []
        y = []
        y_p = []
        x_f = []
        y_f = []
        step = (xmax - xmin) / float(n)
        step_res = (xmax - xmin) / float(resolution)
        for i in xrange(n):
            x.append(xmin + i * step)
        for elem_x in x:
            y.append(f(elem_x))

        for i in xrange(resolution):
            x_f.append(xmin + i * step_res)
        for elem in x_f:
            y_f.append(f(elem))

        for elem_x in x:
            y_p.append(self.p_L(elem_x, x, y))

        plt.plot(x, y_p, 'ro')
        plt.plot(x_f, y_f, '.')
        plt.axis(axis)
        plt.show()

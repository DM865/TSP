#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:29:58 2018

@author: marco
"""

# %matplotlib inline
import matplotlib.pyplot as plt
import random
import time
import itertools
import urllib
import csv
# import functools
from statistics import mean, stdev


# Cities are represented as Points, which are a subclass of complex numbers

class Point(complex):
    x = property(lambda p: p.real)
    y = property(lambda p: p.imag)
    
City = Point

def distance(A, B): 
    "The distance between two points."
    return abs(A - B)

def Cities(n, width=900, height=600, seed=42):
    "Make a set of n cities, each with random coordinates within a (width x height) rectangle."
    random.seed(seed * n)
    return frozenset(City(random.randrange(width), random.randrange(height)) for c in range(n))

def Maps(num_maps, num_cities):
    "Return a tuple of maps, each consisting of the given number of cities."
    return tuple(Cities(num_cities, seed=(m, num_cities)) for m in range(num_maps))

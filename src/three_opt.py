#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:55:34 2018

@author: marco
"""


import sys
from data import *

from solutions import *
from c_heuristics import *



def three_opt_canonical(cities):
    "Construct canonical solution, and alter the results by three opt."
    tour=[c for c in cities]
    return three_opt(tour)


def three_opt(tour):
    "Iterative improvement based on 3 exchange."
    "Write your code here"
    return tour

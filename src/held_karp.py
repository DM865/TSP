#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:50:19 2018

@author: marco
"""

import functools
from solutions import *


def hk_tsp(cities):
    """The H eld-Karpshortest tour of this set of cities.
    For each end city C, find the shortest segment from A (the start) to C.
    Out of all these shortest segments, pick the one that is the shortest tour."""
    A = first(cities)
    return shortest_tour(shortest_segment(A, cities - {A, C}, C)
                         for C in cities if C is not A)

@functools.lru_cache(None)
def shortest_segment(A, Bs, C):
    "The shortest segment starting at A, going through all Bs, and ending at C."
    print(A,Bs,C)
    if not Bs:
        return [A, C]
    else:
        segments = [shortest_segment(A, Bs - {B}, B) + [C] for B in Bs]
        return min(segments, key=segment_length)
            
def segment_length(segment):
    "The total of distances between each pair of consecutive cities in the segment."
    # Same as tour_length, but without distance(tour[0], tour[-1])
    return sum(distance(segment[i], segment[i-1]) for i in range(1, len(segment)))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:38:45 2018

@author: marco
"""

from data import *

def dq_tsp(cities):
    """Find a tour by divide and conquer: if number of cities is 3 or less,
    any tour is optimal.  Otherwise, split the cities in half, solve each
    half recursively, then join those two tours together."""
    if len(cities) <= 3:
        return Tour(cities)
    else:
        Cs1, Cs2 = split_cities(cities)
        return join_tours(dq_tsp(Cs1), dq_tsp(Cs2))
    
    
def split_cities(cities):
    "Split cities vertically if map is wider; horizontally if map is taller."
    width, height = extent([c.x for c in cities]), extent([c.y for c in cities])
    key = 'x' if (width > height) else 'y'
    cities = sorted(cities, key=lambda c: getattr(c, key))
    mid = len(cities) // 2
    return frozenset(cities[:mid]), frozenset(cities[mid:])

def extent(numbers): return max(numbers) - min(numbers)



def join_tours(tour1, tour2):
    "Consider all ways of joining the two tours together, and pick the shortest."
    segments1, segments2 = rotations(tour1), rotations(tour2)
    tours = [s1 + s2
             for s1 in segments1
             for s  in segments2
             for s2 in (s, s[::-1])]
    return shortest_tour(tours)

def rotations(sequence):
    "All possible rotations of a sequence."
    # A rotation is some suffix of the sequence followed by the rest of the sequence.
    return [sequence[i:] + sequence[:i] for i in range(len(sequence))]

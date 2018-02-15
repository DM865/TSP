#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:38:45 2018

@author: marco
"""

import data
import itertools


def alltours_tsp(cities):
    "Generate all possible tours of the cities and choose the shortest tour."
    return shortest_tour(alltours(cities))

def shortest_tour(tours): 
    "Choose the tour with the minimum tour length."
    return min(tours, key=tour_length)


alltours = itertools.permutations 


def alltours(cities):
    "Return a list of tours, each a permutation of cities, but each one starting with the same city."
    start = first(cities)
    return [[start] + Tour(rest)
            for rest in itertools.permutations(cities - {start})]

def first(collection):
    "Start iterating over collection, and return the first element."
    return next(iter(collection))

Tour = list  # Tours are implemented as lists of cities



def nn_tsp(cities, start=None):
    """Start the tour at the first city; at each step extend the tour 
    by moving from the previous city to its nearest neighbor 
    that has not yet been visited."""
    if start is None: start = first(cities)
    tour = [start]
    unvisited = set(cities - {start})
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour


def nearest_neighbor(A, cities):
    "Find the city in cities that is nearest to city A."
    return min(cities, key=lambda c: distance(c, A))


def repeated_nn_tsp(cities, repetitions=100):
    "Repeat the nn_tsp algorithm starting from specified number of cities; return the shortest tour."
    return shortest_tour(nn_tsp(cities, start) 
                         for start in sample(cities, repetitions))

def sample(population, k, seed=42):
    "Return a list of k elements sampled from population. Set random.seed with seed."
    if k is None or k > len(population): 
        return population
    random.seed(len(population) * k * seed)
    return random.sample(population, k)







def greedy_tsp(cities):
    """Go through edges, shortest first. Use edge to join segments if possible."""
    endpoints = {c: [c] for c in cities} # A dict of {endpoint: segment}
    for (A, B) in shortest_edges_first(cities):
        if A in endpoints and B in endpoints and endpoints[A] != endpoints[B]:
            new_segment = join_endpoints(endpoints, A, B)
            if len(new_segment) == len(cities):
                return new_segment
            
            
def shortest_edges_first(cities):
    "Return all edges between distinct cities, sorted shortest first."
    edges = [(A, B) for A in cities for B in cities 
                    if id(A) < id(B)]
    return sorted(edges, key=lambda edge: distance(*edge))


def join_endpoints(endpoints, A, B):
    "Join B's segment onto the end of A's and return the segment. Maintain endpoints dict."
    Asegment, Bsegment = endpoints[A], endpoints[B]
    if Asegment[-1] is not A: Asegment.reverse()
    if Bsegment[0] is not B: Bsegment.reverse()
    Asegment.extend(Bsegment)
    del endpoints[A], endpoints[B] # A and B are no longer endpoints
    endpoints[Asegment[0]] = endpoints[Asegment[-1]] = Asegment
    return Asegment





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





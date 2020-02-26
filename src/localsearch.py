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


def evaluate_change(tour, i, j):
    "evaluate if reversing tour[i:j] would make the tour shorter."
    A, B, C, D = tour[i], tour[i+1], tour[j], tour[(j+1) % len(tour)]
    # Are old edges (AB + CD) longer than new ones (AC + BD)? If so, reverse segment.
    delta = distance(A, C) + distance(B, D) - distance(A, B) - distance(C, D)
    return delta


def commit_change(tour, i, j):
    # Given tour [...A-B...C-D...], reverse B...C to get [...A-C...B-D...]
    tour[(i+1):(j+1)] = reversed(tour[(i+1):(j+1)])


def two_opt(tour):
    "Try to alter tour for the better by reversing segments."
    incumbent_length = tour_length(tour)
    improvement = True
    while improvement:
        improvement = False
        for (start, end) in all_segments(len(tour)):
            delta = evaluate_change(tour, start, end)
            if delta < 0:
                commit_change(tour, start, end)
                incumbent_length = incumbent_length + delta
                if abs(tour_length(tour) - incumbent_length) > 1e-8:  # useful for debugging! remove in production
                    print("different: ", tour_length(tour), incumbent_length)
                    sys.exit(0)
                improvement = True

                print(start, end, incumbent_length)
    # plot_tour(tour)
    return tour


def all_segments(N):
    "Generator that returns (start, end) pairs of indexes that form segments of tour of length N."
    # return ((start, start + length)
    #        for length in range(N, 2-1, -1)
    #        for start in range(N - length + 1))
    return ((i, j) for (i, j) in itertools.combinations(range(N), 2) if j != i+1)
    # equivalent form:
    # for (i, j) in itertools.combinations(range(N), 2):
    #    if j == i+1:
    #        continue
    #    yield (i, j)


def altered_nn_tsp(cities):
    "Run nearest neighbor TSP algorithm, and alter the results by reversing segments."
    return two_opt(nn_tsp(cities))


def altered_greedy_tsp(cities):
    "Run greedy TSP algorithm, and alter the results by reversing segments."
    return two_opt(greedy_tsp(cities))


def altered_canonical(cities):
    "Construct a canonical solution and alter the result by reversing segments."
    tour = [c for c in cities]
    return two_opt(tour)

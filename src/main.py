#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:50:19 2018

@author: marco
"""

import data
import algorithms
import assessment
import benchmarking


def length_ratio(cities): 
    "The ratio of the tour lengths for nn_tsp and alltours_tsp algorithms."
    return tour_length(nn_tsp(cities)) / tour_length(alltours_tsp(cities))

sorted(length_ratio(Cities(8, seed=i*i)) for i in range(11))

def repeat_10_nn_tsp(cities): return repeated_nn_tsp(cities, 10)
def repeat_100_nn_tsp(cities): return repeated_nn_tsp(cities, 100)
def repeat_25_nn_tsp(cities): return repeated_nn_tsp(cities, 25)
def repeat_50_nn_tsp(cities): return repeated_nn_tsp(cities, 50)


def altered_mst_tsp(cities): return alter_tour(mst_tsp(cities))



algorithms = [nn_tsp, repeat_10_nn_tsp, repeat_25_nn_tsp, repeat_50_nn_tsp, repeat_100_nn_tsp]

benchmarks(algorithms, Maps(30, 60))


algorithms = [altered_nn_tsp, altered_greedy_tsp, repeated_altered_nn_tsp]

benchmarks(algorithms)
print('-' * 100)
benchmarks(algorithms, Maps(30, 120))
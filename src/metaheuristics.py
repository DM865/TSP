#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:55:34 2018

@author: marco
"""

from data import *
from solutions import *

from c_heuristics import *
from localsearch import *




def repeated_nn_tsp(cities, repetitions=100):
    "Repeat the nn_tsp algorithm starting from specified number of cities; return the shortest tour."
    return shortest_tour(nn_tsp(cities, start) for start in sample(cities, repetitions))

def sample(population, k, seed=42):
    "Return a list of k elements sampled from population. Set random.seed with seed."
    if k is None or k > len(population): 
        return population
    random.seed(len(population) * k * seed)
    return random.sample(population, k)




def repeated_altered_nn_tsp(cities, repetitions=20): 
    "Use alteration to improve each repetition of nearest neighbors."
    return shortest_tour(alter_tour(nn_tsp(cities, start)) 
                         for start in sample(cities, repetitions))

def repeat_5_altered_nn_tsp(cities): return repeated_altered_nn_tsp(cities, 5)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:50:19 2018

@author: marco
"""

import sys

from data import *
from data2 import *
from solutions import *

from enumeration import *
from dq import *
from held_karp import *

from c_heuristics import *
from localsearch import *
from three_opt import *
from metaheuristics import *

from benchmarking import *

print(hk_tsp(Cities(5,seed=1)))
#plot_lines(USA_map, 'bo')
#plt.show()
#plot_tsp(altered_canonical,USA_map)
#plt.show()
# altered_canonical(Cities(30,seed=1))
#altered_canonical(USA_map)
sys.exit(0)


algorithms = [hk_tsp]
benchmarks(algorithms, Maps(2, 10))

sys.exit(0)

#algorithms = [three_opt_canonical]
algorithms = [greedy_tsp, nn_tsp]
benchmarks(algorithms, tuple(USA_map for i in range(10)))


# print(hk_tsp(Cities(5,seed=1)))

sys.exit(0)


def length_ratio(cities):
    "The ratio of the tour lengths for nn_tsp and alltours_tsp algorithms."
    return tour_length(nn_tsp(cities)) / tour_length(alltours_tsp(cities))

#print(sorted(length_ratio(Cities(8, seed=i*i)) for i in range(11)))

# sys.exit(0)


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

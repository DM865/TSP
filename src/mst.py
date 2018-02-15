#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 19:16:37 2018

@author: marco
"""

def mst(vertexes):
    """Given a set of vertexes, build a minimum spanning tree: a dict of the form {parent: [child...]}, 
    where parent and children are vertexes, and the root of the tree is first(vertexes)."""
    tree  = {first(vertexes): []} # the first city is the root of the tree.
    edges = shortest_edges_first(vertexes)
    while len(tree) < len(vertexes):
        (A, B) = shortest_usable_edge(edges, tree)
        tree[A].append(B)
        tree[B] = []
    return tree

def shortest_usable_edge(edges, tree):
    "Find the ehortest edge (A, B) where A is in tree and B is not."
    (A, B) = first((A, B) for (A, B) in edges if (A in tree) ^ (B in tree)) # ^ is "xor" 
    return (A, B) if (A in tree) else (B, A)

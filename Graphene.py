# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:13:19 2020

@author: masou
"""

""" 
Prt2
preface: We extend our Molecule class to be able to calculate the various properties of types of Graphene
"""

from Huckel import Molecule, a, b
import numpy as np
import matplotlib.pyplot as plt
import copy

class Carbon:
    def __init__(self, x, y, magnitudes, id):
        self.pos = (x, y)
        self.psi_magnitudes = magnitudes
        self.id = id     # Which carbon atom it is?

class Graphene(Molecule):
    def __init__(self, *args):
        super(Graphene, self).__init__(*args)
        self.carbons = []   # List of Carbon Atoms
        self.prev_id = 0    # Stores the id of the most recntly generated carbon 
        self.current_row = 1    # Stores the row of hexagons that the most recentlygenerated carbon belongs to
        
    def generate_carbon(self, id, m, n, position_set):   # m is number of hexagon rows, n is number of hexagon columns
    """Mint a new Carbon atom"""
        mags = [(abs(eig[id - 1][0])**2) for eig in self.eigenvectors]
        position = position_set
        
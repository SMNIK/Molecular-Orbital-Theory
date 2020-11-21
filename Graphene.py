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
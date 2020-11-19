# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:11:07 2020

@author: masou
"""

# Project: Molecular Orbital Theory (MOT)

import numpy as np 
from numpy import linalg as lig
import sympy as smp
import matplotlib.pyplot as plt
from perator import itemgetter
import collections

"""
preface:
    Part 1 - Huckel(H) theory for pi-molecular orbitals.
    for a given matrix H, with Alpha diagonals and Beta off-diagonals,
    we will determine the Eigenvalues and Eigenvectors.
    For the Huckel Effective Hamiltonian and use to them to create an energy
    level diagram for the electronic configuration of the molecule.
"""

a,b = smp.symbols('a,b') # General symbols so we can use them in our fancy matrix

class Molecule:
    """This class represents a molecule with a Huckel Matrix and associated methods"""
    
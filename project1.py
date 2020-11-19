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
    
    def __init__(self, name, H, num_pi_electrons, num_carbons, num_double_bonds):
        self.H = H
        self.name = name
        self.num_carbons = num_carbons
        self.eigenvalues = []
        self.eigenvectors = []
        self.normalized_eigenvectors = []
        self.eigval_eigvect = []     # Associate Eigenvalue with its Eigenvect
        self.eigval_multiplicity = []
        self.num_pi_electrons = num_pi_electrons
        self.deloc_energy = 0.0
        self.alpha = None
        self.beta = None
        self.charge_density = []
        self.bond_order = []
        self.num_additional_connections = 0
        self.con = []
        self.num_double_bonds = num_double_bonds

        # This is our internal data structure that contains [(eig_value, of electrons)]   
        self.e_per_energy_lvl = []
        self.e_per_eigen_vect = []
        
    def __str__(self):
        """Creat the string represtation for the molecule"""
        return "---" + self.name + "--- \n" + str(self.H) + "\n" \
                + "Charge Density :" + str(self.charge_density) + "\n" \
                + "Delocalization Energy :" + str(self.deloc_energy) + "\n" \
                + "Bond Order :" +str(self.bond_order) + "\n"
                
    def set_constants(self, al, be):
        """This function substitutes numeric value in place for Alpha and Beta in the Huckel Matrix"""
        
        # Replace our H matrix with numerical values
        self.H = np.matrix([[al if x ==a else be if x==b else x for x in i] for i in self.H.tolist()])
        
        # Store the resonance integral values
        self.alpha = al
        self.beta = be
        
    def generate_H(self):
        """generates H matrix for linear carbon chain"""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
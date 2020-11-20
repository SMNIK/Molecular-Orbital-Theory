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
        N = self.num_carbons
        H = np.zeros((N, N)).tolist()
        
        for i in range(N):
            H[i][i] = a
            if i==0:
                H[i][i+1] = b
            elif i == N - 1:
                H[i][i-1] = b
            else:
                H[i][i+1] = b
                H[i][i-1] = b
                
        self.H = np.matrix(H)
        
    def add_connections(self, con):
        """adds con to the Huckel matrix, takes a list of lists and inserts
           beta into H at the specified coordinates
           con: [[coord1, coord2]...]
        """
        self.con = con
        for i in range(len(con)):
            self.H[con[i][0] - 1, con[i][1] - 1] = b
            self.H[con[i][1] - 1, con[i][0] - 1] = b
        self.num_additional_connections += len(con)
        
    def delete_connections(self, con):
        """deletes con to the Huckel matrix, takes a list of tuples and
           inserts zero into H at the specified coordinates
           con: [[coord1, coord2]...]
        """
        for i in range(len(con)):
            self.H[con[i][0] - 1, con[i][1] - 1] = 0
            self.H[con[i][1] - 1, con[i][0] - 1] = 0
        self.num_additional_connections -= len(con)
        
    def generate_eigen(self):
        """Finds the eigenvalue and eigenvector for the H matrix"""
        assert(self.alpha is not None and self.beta is not None)  # We are no longer using symbolic evals
        
        # REset our arrays
        self.eigenvalues = []
        self.eigenvectors = []
        self.eigval_multiplicity = []
        self.eigval_eigvect = []
        
        e_vals, e_vects = lig.eig(self.H)   # Generate using Numpy's eigenvals
        e_vals = np.around(e_vals, decimals=5)   # Round these eigen values
        freq_dict = collections.Counter(e_vals)   # Count up of Eigenvalue and their multiplicity
        
        # Store the eigenvalues alonf=g with their multiplicities. Note: Eigenvalues in this array is unique
        self.eigval_multiplicity = sorted(freq_dict.items(), key=lambda x: x[0])

        # Associate each eigenvalues with their eigenvectors. Note: Eigenvalues may repeat in this array
        for i in range(len(e_vals)):
            eigenvalue = e_vals[i]
            mega_tuple = tuple([eigenvalue, e_vects[:, i]])
            self.eigval_eigvect.append(mega_tuple)
            
        # Sort our eigval_eigvect list, in ascending eigenvalue order
        self.eigval_eigvect.sort(key=lambda x: x[0])
        
        # Store just the eigenvalues and the eigenvectors in the appropriate arrays
        for eig_set in self.eigval_eigvect:
            self.eigenvalues = eig_set[0]
            self.eigenvetors.append(eig_set[1].tolist())
            
        # Reset the array which will hold the number of electrons per eigenvalue
        self.e_per_energy_lvl = []
        
        # Compile our electron per energy level array
        electrons_available = self.num_pi_electrons
        for eig_val_multiplicity in self.eigval_multiplicity:
            eig_val = eig_val_multiplicity[0]
            multiplicity = eig_val_multiplicity[1]
            if electrons_available >= (multiplicity * 2):
                self.e_per_energy_lvl.append(tuple([eig_val , 2 * multiplicity]))
                electrons_available -= 2 * multiplicity
            else:
                self.e_per_energy_lvl.append(tuple([eig_val, electrons_available]))
                electrons_available -= electrons_available 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
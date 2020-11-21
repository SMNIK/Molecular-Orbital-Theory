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
        if position_set == 'find':
            position = self.find_position(id, m, n)
        return Carbon(position[0], position[1], mags, i)
    
    def zig_zipper(self, m, n):
        """Creates row of linking carbons to wrap zigzag"""
        a = 0.5        # Short leg of 30-60-90 triangle
        b = float((3**(1/2.0))/2.0)     # long len of 30-60-90 triangle
        carb_iter = self.num_carbons - (2*n + 1)
        pull_tab = copy.copy(self.carbons[carb_iter])
        self.carbons[carb_iter + 1].pos = (pull_tab.pos[0], pull_tab.pos[1]-2*b)
        t = copy.copy(self.carbons[carb_iter + 1])
        if m % 2 == 0:
            dist = 2
            for i in range(2*n-1):
                self.carbons[(carb_iter+2+i)].pos = (t.pos[0]-dist, t.pos[1])
                t = copy.copy(self.carbons[(carb_iter+2+i)])
                if dist == 2:
                    dist = 1
                else:
                    dist = 2
        else:
            dist = 2
            for i in range(2*n-1):
                self.carbons[(carb_iter+2+i)].pos = (t.pos[0]+dist, t.pos[1])
                t = copy.copy(self.carbons[(carb_iter+2+i)])
                if dist == 2:
                    dist = 1
                else:
                    dist = 2
                    
    def find_position(self, id, m, n):
        """Finds the x, y carbon of a specific carbon atom"""
        prev = self.prev_id
        xprev = 0
        yprev = 0
        if self.prev_id !=0:
            xprev = self.carbons[prev-1].pos[0]
            yprev = self.carbons[prev-1].pos[1]
        row = self.current_row
        a = 0.5     # Short leg of 30-60-90 triangle
        b = float((3**(1/2.0))/2.0)    # long leg of 30-60-90 triangle
        
        if row == 1:
            if prev == 0:
                xpos = 0.0
                ypos = 0.0
            elif prev == 4*n:
                xpos = xprev - a
                ypos = yprev - b    #(sqrt(3))/2
                self.current_row +=1
            else:
                if prev % 2 == 0:
                    xpos = xprev + 1
                    ypos = yprev
                else:
                    xpos = xprev + a
                    if id % 4 == 0:
                        ypos = yprev - b
                    else:
                        ypos = yprev + b
        elif row == 2:
            if prev == 4*n + (row-1)*(4*n - 1):
                xpos = xprev + a
                ypos = yprev - b
                self.current_row += 1
            else:
                if id % 2 == 0:
                    xpos = xprev - 1
                    ypos = yprev
                else:
                    xpos = xprev - a
                    if (id+row-1) % 4 == 0:
                        ypos = yprev - b
                    else:
                        ypos = yprev + b
                  
        elif row == 3:
            if prev == 4*n + (row-1)*(4*n - 1):
                xpos = xprev 
                ypos = yprev - 2*b
                self.current_row += 1
            elif prev == 4*n + (row-1)*(4*n -1) - 1:
                    xpos = xprev + a
                    ypos = yprev + b
                else:
                    if prev % 2 == 0:
                        xpos = xprev + 1
                        ypos = yprev
                    else:
                        xpos = xprev + a
                        if (id+row-1) % 4 == 0:
                            ypos = yprev - b
                        else:
                            ypos = yprev + b
        elif row == m + 1:
            if id == 4*n + 2*(4*n -1) + (row-3)*(2*n +2):
                if row % 2 == 0:
                    xpos = xprev - a
                    ypos = yprev + b
                else:
                    xpos = xprev + a
                    ypos = yprev + b
            elif prev == 4*n + 2*(4*n -1) + (row-4)*(4*n) + 1:
                ypos = yprev - b  
                if row % 2 == 0:
                    xpos = xprev - a
                else:
                    xpos = xprev + a
            else:
                if row % 2 == 0:
                    if prev % 2 == 0:
                        xpos = xprev - 1
                        ypos = yprev
                    else:
                        xpos = xprev - 2
                        ypos = yprev
                    else:
                        if prev % 2 == 0:
                            xpos = xprev + 1
                            ypos = yprev
                        else:
                            xpos = xprev + 2
                            ypos = yprev
        else:
            if prev == 4*n + 2*(4*n -1) + (row-3)*(4*n):
                xpos = xprev
                ypos = yprev - 2*b
                self.current_row += 1
            elif prev == 4*n + 2*(4*n -1) + (row-3)*(4*n) - 1:
                ypos = yprev + b
                if row % 2 == 0:
                    xpos = xprev - a
                else:
                    xpos = xprev + a
                elif prev == 4*n + 2*(4*n -1) + (row-4)*(4*n) + 1:
                    ypos = yprev - b
                    if row % 2 == 0:
                        xpos = xprev - a
                    else:
                        xpos = xprev + a
                else:
                    if prev % 2 == 0:
                        if row % 2 == 0:
                            xpos = xprev - 1
                            ypos = yprev
                        else:
                            xpos = xprev + 1
                            ypos = yprev
                    else:
                        if row % 2 == 0:
                            xpos = xprev - a
                            if (prev - 1) % 4 ==0:
                                ypos = yprev - b
                            else:
                                ypos = yprev + b
                                
    
    
    
    
    
    
    
    
    
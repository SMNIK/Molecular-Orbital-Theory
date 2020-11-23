# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:36:57 2020

@author: masou
"""

import numpy as np
from Molecule import Molecule

tol = Molecule('Toluene', np.matrix([]), 7, 7, 3)
tol.generate_H()
tol.add_connections([[1, 6]])
tol.set_constants(0, -1)
tol.generate_eigen()
tol.find_deloc_energy()
tol.energy_level_plot()
tol.find_charge_density()
tol.find_bond_order()
print(tol)
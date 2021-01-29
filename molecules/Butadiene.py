# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:24:12 2020

@author: masou
"""

import numpy as np
from Molecule import Molecule, a, b

butadiene_H = np.matrix([[a, b, 0, 0], [b, a, b, 0],[0, b, a, b], [0, 0, b, a]])
butadiene = Molecule('Butadiene', butadiene_H, 4, 4, 2)
butadiene.set_constants(0, -1)
butadiene.generate_eigen()
butadiene.find_deloc_energy()
butadiene.energy_level_plot()
butadiene.find_charge_density()
butadiene.find_bond_order()
print(butadiene)
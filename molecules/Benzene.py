# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:02:07 2020

@author: masou
"""

import numpy as np
from Huckel import Molecule

benzene = Molecule('Benzene', np.matrix([]), 6, 6, 3)
benzene.generate_H()
benzene.add_connections([[1,6]])
benzene.set_constants(0,-1)
benzene.generate_eigen()
benzene.find_deloc_energy()
benzene.energy_level_plot()
benzene.find_charge_density()
benzene.find_bond_order()
print(benzene)
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:31:25 2020

@author: masou
"""

import numpy as np
from Huckel import Molecule

napth = Molecule('Napthalene', np.matrix([]), 10, 10, 5)
napth.generate_H()
napth.add_connections([[5, 10], [1, 6]])
napth.set_constants(0, -1)
napth.generate_eigen()
napth.find_deloc_energy()
napth.energy_level_plot()
napth.find_charge_density()
napth.find_bond_order()
print(napth)
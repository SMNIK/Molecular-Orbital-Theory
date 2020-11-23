# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 10:35:20 2020

@author: masou
"""

import numpy as np
from graphene import Graphene as gra

arm = gra('Armchair', np.matrix([]), 42, 42, 13)
arm.generate_H()
arm.add_connections([[1,22],[4,21],[5,18],[8,17],[9,14],[15,32],[16,29],[19,28],
                     [20,25],[33,35],[31,37],[30,38],[27,39],[26,40],[24,42],[13,34]])
arm.add_connections([[1,12],[23,34],[35,42]])
arm.delete_connections([[34,35],[37,38],[39,40]])
arm.set_constants(0,1)
arm.generate_eigen()
arm.find_charge_density()
arm.find_deloc_energy()
arm.generate_carbons(3,3)

print(arm)

arm.plot_lattice(0)
arm.plot_lattice(1)
arm.plot_lattice(2)
arm.plot_lattice(3)
arm.plot_lattice(4)
arm.plot_lattice(5)
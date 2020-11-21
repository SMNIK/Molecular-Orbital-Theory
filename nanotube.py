# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 11:40:36 2020

@author: masou
"""

from Armchair import arm

# wrap this yp in nanotube
arm.add_connections([[1,12],[23,34],[35,42]])
arm.delete_connections([[34,35],[37,38],[39,40]])
arm.set_constants(0,1)
arm.generate_eigen()
arm.find_charge_density()
arm.find_deloc_energy()
arm.generate_carbons(3,3)

print(arm)
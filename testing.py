# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:15:33 2020

@author: masou
"""
import unittest
import numpy as np
from Molecule import Molecule
from Benzene import benzene

# # class Test(unittest.TestCase):
#     # def test_1(self):
#     #     assert Molecule
#     #     assert Molecule.find_bond_order
#     #     assert Molecule.find_deloc_energy
#     #     assert Molecule.find_charge_density
#     #     assert Molecule.find_nodes
#     #     assert Molecule.set_constants
#     #     assert Molecule.generate_eigen
#     #     assert Molecule.generate_H
#     #     assert Molecule.energy_level_plot
#     #     assert Molecule.delete_connections
#     #     assert Molecule.add_connections
#     #     assert Molecule.__str__
#     #     assert Molecule.__init__

#     # def test_2(self):
# print("B.c_d: ", benzene.charge_density)
# print("a.f_d_e: ", benzene.find_deloc_energy())
# print("a.f_c_d: ", benzene.find_charge_density())
# print("a.f_b_o: ", benzene.find_bond_order())

class Test(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(benzene.name, 0)


if __name__ == "__main__":
    unittest.main()


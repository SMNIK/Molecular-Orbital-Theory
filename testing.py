# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:35:43 2021

@author: masou
"""

import numpy as np
import unittest
from Molecule import Molecule


class TestMolecule(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('set up class Molecule')

    @classmethod
    def setDownClass(cls):
        print('tear down class Molecule\n')

    def setUp(self):
        print('set up Molecule')
        self.valid = Molecule("testing", np.matrix([]), 4, 4, 2)
        self.valid.generate_H()
        self.valid.add_connections([[1, 4]])
        self.valid.set_constants(0, -1)
        self.valid.generate_eigen()
        self.valid.find_deloc_energy()
        self.valid.energy_level_plot()
        self.valid.find_charge_density()
        self.valid.find_bond_order()

    @classmethod
    def tearDown(cls):
        print('tear down Molecule\n')

    def test_set_constants(self):
        print('test set constants')
        Molecule.H = np.matrix([[0, -1], [-1, 0]])
        self.H = np.matrix([])
        Molecule.set_constants(0, -1)
        self.assertEqual(str(Molecule.H), '[[ 0 -1]\n [-1  0]]')


if __name__ == '__main__':
    unittest.main

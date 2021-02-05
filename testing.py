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
        Molecule.set_constants(self, 0, -1)
        self.assertEqual(str(Molecule.H), '[[ 0 -1]\n [-1  0]]')

    def test_generate_H(self):
        print('test generate_H')
        self.num_carbons = 4
        first = str(Molecule.generate_H(self))
        second = '[[a b 0.0 0.0]\n [b a b 0.0]\n [0.0 b a b]\n [0.0 0.0 b a]]'
        self.assertEqual(first, second)

    def test_generate_eigen(self):
        print('test generate_eigen')
        self.alpha = 0
        self.beta = -1
        self.H = [[0, -1, 0, 0], [-1, 0, -1, 0], [0, -1, 0, -1], [0, 0, -1, 0]]
        self.valid.generate_eigen()
        self.assertAlmostEqual(Molecule.generate_eigen(
            self), None, None, None, None)

    def test_add_connections(self):
        print('test add connections')
        self.valid.add_connections([])
        self.assertEqual(str(
            self.valid.H), '[[ 0. -1.  0. -1.]\n [-1.  0. -1.  0.]\n [ 0. -1.  0. -1.]\n [-1.  0. -1.  0.]]')

    def test_e_per_energy_lvl(self):
        print('test e_per_energy_lvl')
        self.num_pi_electrons = 4
        self.eigval_multiplicity = []
        self.assertAlmostEqual(Molecule.e_per_energy_lvl(
            self), None, None, None, None)

    def test_delete_connections(self):
        print('test delete connections')
        self.valid.delete_connections([])
        self.assertEqual(str(
            self.valid.H), '[[ 0. -1.  0. -1.]\n [-1.  0. -1.  0.]\n [ 0. -1.  0. -1.]\n [-1.  0. -1.  0.]]')


if __name__ == '__main__':
    unittest.main

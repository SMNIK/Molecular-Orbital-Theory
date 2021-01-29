# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:35:43 2021

@author: masou
"""

import numpy as np
import unittest
from Molecule import Molecule

class TestBenzene(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('set up class')
        
    @classmethod
    def setDownClass(cls):
        print('tear down class')
        
    def setUp(self):
        print('set up')
        
        self.benzene = Molecule("Benzene", np.matrix([]), 6, 6, 3)
        self.benzene.generate_H()
        self.benzene.add_connections([[1, 6]])
        self.benzene.set_constants(0, -1)
        self.benzene.generate_eigen()
        self.benzene.find_deloc_energy()
        self.benzene.energy_level_plot()
        self.benzene.find_charge_density()
        self.benzene.find_bond_order()
        
    @classmethod
    def tearDown(cls):
        print('tear down\n')
        
    def test_benzene_str(self):
        print('test the __str__ output')
        first = self.benzene.__str__()
        second = str(self.benzene)
        self.assertEqual(first, second)
        
    def test_benzene_coefficients(self):
        print('test all coefficients')
        self.assertAlmostEqual(self.benzene.alpha, 0)
        self.assertAlmostEqual(self.benzene.beta, -1)
        self.assertAlmostEqual(self.benzene.deloc_energy, -2.0)
        self.assertAlmostEqual(self.benzene.eigenvalues, 2.0)
        
    def test_benzene_lists(self):
        print('test the coefficients lists of benzene')
        
        density = [1.02, 0.9, 1.08, 1.02, 0.9, 1.08]
        order = [1.56, 1.65, 1.77, 1.56, 1.65, 1.77]
        for n in range(len(self.benzene.charge_density)):
            first = self.benzene.charge_density[n]
            second = density[n]
            delta = 0.1
            message = 'The charge density elements for testing are not almost equal'
            self.assertAlmostEqual(first, second, None, message, delta)
            
            bond = self.benzene.bond_order[n]
            second1 = order[n]
            message0 = 'The bond order elements for testing are not almost equal'
            self.assertAlmostEqual(bond, second1, None, message0, delta)
        
        
        
        
        
if __name__ == '__main__':
    unittest.main
    
    
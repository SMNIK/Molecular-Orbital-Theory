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
        print('setUp')
        
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
        first = self.bnzene.__str__
        second = str(self.benzene)
        self.assertEqual(first, second)
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    unittest.main
    
    
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
        print('set up class Benzene')

    @classmethod
    def setDownClass(cls):
        print('tear down class Benzene')

    def setUp(self):
        print('set up Benzene')


if __name__ == '__main__':
    unittest.main

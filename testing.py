# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:35:43 2021

@author: masou
"""

import numpy as np
import unittest
from Molecule import Molecule, a, b


class TestBenzene(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('set up class Benzene')

    @classmethod
    def setDownClass(cls):
        print('tear down class Benzene')

    def setUp(self):
        print('set up Benzene')
# specify the benzene molecule (or others) as the test resource for the core of code
# you coud initialize your own molecule but you need to calculate the output and compare with the cod answers
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
        print('tear down Benzene\n')
        
# check if the information in output of Benzene and calable answer are the same or not
    def test_benzene_str(self):
        print('test the __str__ output of benzene')
        first = self.benzene.__str__()
        second = str(self.benzene)
        self.assertEqual(first, second)

    def test_benzene_coefficients(self):
        print('test all coefficients of benzene')
        self.assertAlmostEqual(self.benzene.alpha, 0)
        self.assertAlmostEqual(self.benzene.beta, -1)
        self.assertAlmostEqual(self.benzene.deloc_energy, -2.0)
        self.assertAlmostEqual(self.benzene.eigenvalues, 2.0)

    def test_benzene_lists(self):
        print('test the coefficients lists of benzene')
        # creat a loop to check each elements and decrease the decimal parts or Approximate comparison
        density = [1.02, 0.9, 1.08, 1.02, 0.9, 1.08]
        order = [1.56, 1.65, 1.77, 1.56, 1.65, 1.77]
        for n in range(len(self.benzene.charge_density)):
            first = self.benzene.charge_density[n]
            second = density[n]
            delta = 0.1
            message = 'The charge density elements for testing are not almost equal'
            self.assertAlmostEqual(first, second, None, message, delta)

            bond = self.benzene.bond_order[n]
            second0 = order[n]
            message0 = 'The bond order elements for testing are not almost equal'
            self.assertAlmostEqual(bond, second0, None, message0, delta)
        # this part is a 6*6 matrix or list inside other list so we break it to the basic elements and compare
        eigenvectors = [[[-0.408], [-0.408], [-0.408], [-0.408], [-0.408], [-0.408]], [[-0.577], [-0.289], [0.289], [0.577], [0.289], [-0.289]], [[0.092], [-0.447], [-0.539], [-0.092], [0.447], [0.539]], [[0.577], [-0.289], [-0.289], [0.577], [-0.289], [-0.289]], [[0.062], [-0.528], [0.466], [0.062], [-0.528], [0.466]], [[-0.408], [0.408], [-0.408], [0.408], [-0.408], [0.408]]]
        for m in range(len(self.benzene.eigenvectors)):  # read each list separately
            vectors = self.benzene.eigenvectors[m]
            second1 = eigenvectors[m]
            for i in range(len(vectors)):  # read first deep elements
                vec = vectors[i]
                sec = second1[i]
                # convert the separated lists to the integers elements
                for h in range(len(vec)):
                    v = vec[h]
                    s = sec[h]
                    delta1 = 0.01
                    message1 = 'The eigenvectors elements for testing are not almost equal'
                    self.assertAlmostEqual(v, s, None, message1, delta1)

        self.assertEqual(self.benzene.con, [[1, 6]])
        self.assertEqual(self.benzene.e_per_energy_lvl, [
                         (-2.0, 2), (-1.0, 4), (1.0, 0), (2.0, 0)])
        self.assertEqual(self.benzene.eigval_multiplicity, [
                         (-2.0, 1), (-1.0, 2), (1.0, 2), (2.0, 1)])

# second class for the second molecule testing
class TestButadiene(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('set up class Butadiene')

    @classmethod
    def setDownClass(cls):
        print('tear down class Butadiene')

    def setUp(self):
        print('set up Butadiene')
        self.butadiene_H = np.matrix([[a, b, 0, 0], [b, a, b, 0],[0, b, a, b], [0, 0, b, a]])
        self.butadiene = Molecule('Butadiene', self.butadiene_H, 4, 4, 2)
        self.butadiene.set_constants(0, -1)
        self.butadiene.generate_eigen()
        self.butadiene.find_deloc_energy()
        self.butadiene.energy_level_plot()
        self.butadiene.find_charge_density()
        self.butadiene.find_bond_order()
    
    @classmethod
    def tearDown(cls):
        print('tear down Butadiene\n')

    def test_butadiene_str(self):
        print('test the __str__ output of butadiene')
        first = self.benzene.__str__()
        second = str(self.benzene)
        self.assertEqual(first, second)
    
    def test_butadiene_coefficients(self):
        print('test all coefficients of butadiene')
        self.assertAlmostEqual(self.butadiene.alpha, 0)
        self.assertAlmostEqual(self.butadiene.beta, -1)
        self.assertAlmostEqual(self.butadiene.deloc_energy, -0.47, None, None, 0.1)
        self.assertAlmostEqual(self.butadiene.eigenvalues, 1.62, None, None, 0.2)
        
    def test_butadiene_lists(self):
        print('test the coefficients lists of butadiene')
        density = [1, 1, 1, 1]
        for n in range(len(self.butadiene.charge_density)):
            first = self.butadiene.charge_density[n]
            second = density[n]
            delta = 0.1
            message = 'The charge density elements for testing are not almost equal'
            self.assertAlmostEqual(first, second, None, message, delta)
        
        bond = [1.89, 1.45, 1.89]
        for n in range(len(self.butadiene.bond_order)):
            first = self.butadiene.bond_order[n]
            second = bond[n]
            delta = 0.1
            message = 'The bond_order elements for testing are not almost equal'
            self.assertAlmostEqual(first, second, None, message, delta)
        
        eigenvectors = [[[0.372], [0.602], [0.602], [0.372]], [[-0.602], [-0.372], [0.372], [0.602]], [[0.602], [-0.372], [-0.372], [0.602]], [[-0.372], [0.602], [-0.602], [0.372]]]
        for m in range(len(self.butadiene.eigenvectors)):  # read each list separately
            vectors = self.butadiene.eigenvectors[m]
            second1 = eigenvectors[m]
            for i in range(len(vectors)):  # read first deep elements
                vec = vectors[i]
                sec = second1[i]
                # convert the separated lists to the integers elements
                for h in range(len(vec)):
                    v = vec[h]
                    s = sec[h]
                    delta1 = 0.01
                    message1 = 'The eigenvectors elements for testing are not almost equal'
                    self.assertAlmostEqual(v, s, None, message1, delta1)
        
        
if __name__ == '__main__':
    unittest.main

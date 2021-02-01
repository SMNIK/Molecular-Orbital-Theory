# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:35:43 2021

@author: masou
"""

import numpy as np
import unittest
from Molecule import Molecule, a, b

""" For testing the Molecule file which is the core of this program,
I used the Benzene and Butadiene molecules data to test the outputs of 
Molecule's functions """

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
        order = [1.58, 1.65, 1.77, 1.58, 1.65, 1.77]
        for s in range(len(self.benzene.charge_density)):
            first = self.benzene.charge_density[s]
            second4 = density[s]
            message = 'The charge density elements for testing are not almost equal'
            self.assertAlmostEqual(first, second4, 2, message, None)

            bond = self.benzene.bond_order[s]
            second5 = order[s]
            message0 = 'The bond order elements for testing are not almost equal'
            self.assertAlmostEqual(bond, second5, 2, message0, None)
        
        # this part is a 6*6 matrix or list inside other list so we break it to the basic elements and compare
        eigenvectors = [[[-0.408], [-0.408], [-0.408], [-0.408], [-0.408], [-0.408]], [[-0.577], [-0.289], [0.289], [0.577], [0.289], [-0.289]], [[0.092], [-0.447], [-0.539], [-0.092], [0.447], [0.539]], [[0.577], [-0.289], [-0.289], [0.577], [-0.289], [-0.289]], [[0.062], [-0.528], [0.466], [0.062], [-0.528], [0.466]], [[-0.408], [0.408], [-0.408], [0.408], [-0.408], [0.408]]]
        for m in range(len(self.benzene.eigenvectors)):  # read each list separately
            vectors = self.benzene.eigenvectors[m]
            second1 = eigenvectors[m]
            for i in range(len(vectors)):  # read first deep elements
                vec = vectors[i]
                sec1 = second1[i]
                # convert the separated lists to the integers elements
                for h in range(len(vec)):
                    v = vec[h]
                    s1 = sec1[h]
                    delta1 = 0.01
                    message1 = 'The eigenvectors elements for testing are not almost equal'
                    self.assertAlmostEqual(v, s1, None, message1, delta1)

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
        fir = self.butadiene.__str__()
        seco = str(self.butadiene)
        self.assertEqual(fir, seco)
    
    def test_butadiene_coefficients(self):
        print('test all coefficients of butadiene')
        self.assertAlmostEqual(self.butadiene.alpha, 0)
        self.assertAlmostEqual(self.butadiene.beta, -1)
        self.assertAlmostEqual(self.butadiene.deloc_energy, -0.47, None, None, 0.1)
        self.assertAlmostEqual(self.butadiene.eigenvalues, 1.62, None, None, 0.2)
        
    def test_butadiene_lists(self):
        print('test the coefficients lists of butadiene')
        density = [1, 1, 1, 1]
        for d in range(len(self.butadiene.charge_density)):
            firs = self.butadiene.charge_density[d]
            secon = density[d]
            delta = 0.1
            message = 'The charge density elements for testing are not almost equal'
            self.assertAlmostEqual(firs, secon, None, message, delta)
        
        bond = [1.89, 1.45, 1.89]
        for z in range(len(self.butadiene.bond_order)):
            orde = self.butadiene.bond_order[z]
            second0 = bond[z]
            delta = 0.1
            message = 'The bond_order elements for testing are not almost equal'
            self.assertAlmostEqual(orde, second0, None, message, delta)
        
        eigenvectors = [[[0.372], [0.602], [0.602], [0.372]], [[-0.602], [-0.372], [0.372], [0.602]], [[0.602], [-0.372], [-0.372], [0.602]], [[-0.372], [0.602], [-0.602], [0.372]]]
        for v in range(len(self.butadiene.eigenvectors)):  # read each list separately
            vectors = self.butadiene.eigenvectors[v]
            second1 = eigenvectors[v]
            for k in range(len(vectors)):  # read first deep elements
                vec = vectors[k]
                sec = second1[k]
                # convert the separated lists to the integers elements
                for o in range(len(vec)):
                    v = vec[o]
                    s1 = sec[o]
                    delta1 = 0.01
                    message1 = 'The eigenvectors elements for testing are not almost equal'
                    self.assertAlmostEqual(v, s1, None, message1, delta1)

# to have the separate elements of tuple inside a list we could act like below
        lvl = [(-1.62, 2), (-0.62, 2), (0.62, 0), (1.62, 0)]
        for l in range(len(self.butadiene.e_per_energy_lvl)):
            energ = self.butadiene.e_per_energy_lvl[l]
            second2 = lvl[l]
            for x in range(len(energ)):
                en = energ[x]
                s2 = second2[x]
                delta = 0.01
                message = "first and second are not almost equal."
                self.assertAlmostEqual(en, s2, None, message, delta)
        
        multi = [(-1.62, 1), (-0.62, 1), (0.62, 1), (1.62, 1)]
        for z in range(len(self.butadiene.eigval_multiplicity)):
            eigval = self.butadiene.eigval_multiplicity[z]
            second3 = multi[z]
            for g in range(len(eigval)):
                ei = eigval[g]
                s3 = second3[g]
                delta = 0.01
                message = "first and second are not almost equal."
                self.assertAlmostEqual(ei, s3, None, message, delta)
        
if __name__ == '__main__':
    unittest.main

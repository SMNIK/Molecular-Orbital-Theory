# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:15:33 2020

@author: masou
"""
from Molecule import Molecule
import unittest


class Test(unittest.TestCase):
    def test(self):
        assert Molecule
        assert Molecule.find_bond_order
        assert Molecule.find_deloc_energy
        assert Molecule.find_charge_density
        assert Molecule.find_nodes
        assert Molecule.set_constants
        assert Molecule.generate_eigen
        assert Molecule.generate_H
        assert Molecule.energy_level_plot
        assert Molecule.delete_connections
        assert Molecule.add_connections
        assert Molecule.__str__
        assert Molecule.__init__

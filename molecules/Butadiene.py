# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:24:12 2020

@author: masou
"""

import numpy as np
from Huckel import Molecule, a, b

butadiene_H = np.matrix([[a, b, 0, 0], [b, a, b, 0],[0, b, a, b], [0, 0, b, a]])
butadiene = Molecule('Butadiene', butadiene_H, 4, 4, 2)

butadiene.set_constants(0, -1)
butadiene.generate_eigen()

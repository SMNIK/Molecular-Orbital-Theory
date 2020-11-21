# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:36:57 2020

@author: masou
"""

import numpy as np
from Huckel import Molecule, a, b

tol = Molecule('Toluene', np.matrix([]), 7, 7, 3)
tol.generate_H()
tol.
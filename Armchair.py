# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 11:06:29 2020

@author: masou
"""

from graphene import Graphene as gra
import numpy as np

arm = gra('Armcahir', np.matrix([]), 42, 42 ,13)
arm.generate_H()
arm.add_connections([[1,22],[4,21],[5,18],[8,17],[9,14],[15,32],[16,29],[19,28],
                     [20,25],[33,35],[31,37],[30,38],[27,39],[26,40],[24,42],[13,34]])
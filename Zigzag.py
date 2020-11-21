# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:46:28 2020

@author: masou
"""
from Graphene import Graphene as gra
import numpy as np

zig = gra('ZigZag', np.matrix([]), 48, 48, 18)
zig.generate_H()
zig.add_connections([[1,22],[4,21],[5,18],[8,17],[9,14],[15,32],[16,29],[19,28],
                     [20,25],[33,35],[31,37],[30,38],[27,39],[26,40],[24,42],[13,34]])

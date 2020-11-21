# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:46:28 2020

@author: masou
"""
from Graphene import Graphene as gra
import numpy as np

zig = gra('ZigZag', np.matrix([]), 48, 48, 18)
zig.generate_H()


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
zig.delete_connections([[34,35],[37,38],[39,40],[42,43],[43,44],[44,45],[45,46],[46,47],[47,48]])
zig.add_connections([[41,43],[40,44],[39,45],[38,46],[37,47],[36,48],[43,2],[44,3],[45,6],[46,7],
                     [47,10],[48,11]])
zig.set_constants(0,1)


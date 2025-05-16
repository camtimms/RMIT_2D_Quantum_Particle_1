#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:06:17 2020

@author: e38496
"""


#
# Example of creating arrays of x and y coordinates using mgrid
# in python
#

import numpy as np

N = 4

xyarrays = np.mgrid[:N,:N] 
x = xyarrays[0]
y = xyarrays[1]

# print(x[1:4,1:4])
# print(y[1:4,1:4])


#
# how to circularly shift array values
#

shift = -(N//2)
xshift = np.roll( x, shift, 0)
yshift = np.roll( y, shift, 1)
print(xshift[0:4,0:4])
print(yshift[0:4,0:4])

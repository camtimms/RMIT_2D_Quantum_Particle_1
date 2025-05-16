#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:09:14 2020

@author: e38496
"""


#
# Example of displaying a 2D array as an image
#

import numpy as np
import matplotlib.pyplot as plt

# set an array size
N = 100

# make an array with some real values in it
array = np.outer( np.sin(np.arange(N)*6*np.pi/float(N)), 
                     np.cos(np.arange(N)*3*np.pi/float(N)))

# display the array
plt.imshow(array)

# add a colourbar
plt.colorbar()

# add x and y labels
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.draw()
plt.show()
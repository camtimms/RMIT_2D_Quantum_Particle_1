#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:13:14 2020

@author: e38496
"""


#
# Fourier transform example
#
import numpy as np
import matplotlib.pyplot as plt


# set an array size
N = 100

# make an array with some real values in it
array = np.outer( np.sin(np.arange(N)*55.5*np.pi/float(N)), 
                     np.cos(np.arange(N)*13.4*np.pi/float(N)))

# take the Fourier transform
farray = np.fft.fft2( array )

# display the function
plt.imshow( np.real(array) )
plt.title( "original function")

plt.figure()
# display the real part of the Fourier transform
plt.imshow( np.real(farray) )
plt.title( "Fourier transform")
plt.draw()
plt.show()

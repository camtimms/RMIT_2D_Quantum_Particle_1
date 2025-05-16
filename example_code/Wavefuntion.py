# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:34:27 2023

@author: Campbell Timms
"""

import numpy as np

# define the wavefunction on a grid
x = np.linspace(-5, 5, 1000)
psi = np.exp(-x**2/2)

# compute the normalization constant
dx = x[1] - x[0]  # grid spacing
C = np.sqrt(np.sum(np.abs(psi)**2) * dx)

# normalize the wavefunction
psi_norm = psi / C

# plot the original and normalized wavefunctions
import matplotlib.pyplot as plt
plt.plot(x, np.abs(psi)**2, label='Unnormalized')
plt.plot(x, np.abs(psi_norm)**2, label='Normalized')
plt.legend()
plt.show()

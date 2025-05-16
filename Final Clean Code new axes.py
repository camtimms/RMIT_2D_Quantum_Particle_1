# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:46:34 2023

@author: Campbell Timms
"""

import numpy as np
import matplotlib.pyplot as plt

#Define values

N = 100
# N = Number of pixels/grid size
L = 2
# L = real space constant 
sigma = 0.1
#sigma value found in the Gaussian 
delta_t = 200
#change in time
m = (0.0005485803*1.660566*10**-27)
#m-mass electron = 0.0005485803 (amu) * 1 amu =	1.660566E-27	kg
hbar = 1.054571817*10**-34
#constant hbar: 1.054 571 817...x 10-34 J s or 6.582 119 569...  x 10-16 eV s 
k = 100
#quickness in space
nplot = 6
#number of plots produced by code

xyarrays = np.mgrid[:N,:N] 
x = xyarrays[0]
y = xyarrays[1]
X = (L)*(x - x[N-1,N-1]/2)
Y = (L)*(y - y[N-1,N-1]/2)

# Define the wave function as a Gaussian
r = np.sqrt(X**2+Y**2)
gaussian = np.exp(-r**2/(2*sigma**2))
wavefunction = np.array(gaussian, dtype=complex)

# Normalize the wavefunction 
A_wavefunction = np.sum((wavefunction)**2) 
N_constant = 1/np.sqrt(A_wavefunction)
N_wavefunction = wavefunction*N_constant

#Take the Fourier transform of the wavefunction at t=0.
F_wavefunction = np.fft.fft2(N_wavefunction)

xyarrays = np.mgrid[:N,:N] 
q_x = xyarrays[0]
q_y = xyarrays[1]
q_X = (q_x - q_x[N-1,N-1]/2)
q_Y = (q_y - q_y[N-1,N-1]/2)

shift = N//2
q_xshift = np.roll( q_X, int(-shift), 0)
q_yshift = np.roll( q_Y, int(-shift), 1)

#Use the q-space arrays to make a complex array that stores the values of the free space equation 
qr2 = np.sqrt(q_xshift**2 + q_yshift**2)
Schro_time = np.exp((1j*hbar*delta_t/(2*m))*qr2**2)
qspace = np.array(Schro_time, dtype=complex)

# Multiply the Fourier transform of the wave function by the phase factor
F_wavefunctiont = F_wavefunction*Schro_time

# Take the inverse Fourier transform. 
wavefunctiont = np.fft.ifft2(F_wavefunctiont)

# Initialise the wave function to a Gaussian form times a linear phase term    
x0 = N/2
x_move = Y+x0
int_gaus = N_constant*np.exp((-(x_move**2+X**2)/2*sigma**2)+1j*k*Y)

#Evolve this wave function in time and plot the absolute value of the wave function at several times
t=0

for i in range(nplot):
    delta_t=200
    delta_t = t + delta_t*i
    
    int_gaus = N_constant*np.exp((-(x_move**2+X**2)/2*sigma**2+1j*k*Y))
    Schro_time = np.exp((1j*hbar*delta_t/(2*m))*qr2**2)
    F_wavefunction_new = np.fft.fft2(int_gaus)
    F_wavefunctiont_new = F_wavefunction_new*Schro_time
    new_wavefunctiont = np.fft.ifft2(F_wavefunctiont_new)
        
    plt.imshow(abs(new_wavefunctiont))
    plt.title('' + ' ' + 't=' + str(delta_t))
    
    plt.xlim(0,N)
    plt.xlabel('Arbitary Spatial Units') 
    
    plt.ylim(0,N)   
    plt.ylabel('Arbitary Spatial Units')
    
    plt.colorbar()
    plt.show()
    

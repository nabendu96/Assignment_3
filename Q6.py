# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:00:17 2020

@author: nabendu
"""

#Problem 1
#Fourier Transform of a constant function using numpy

import numpy as np
import cmath
import matplotlib.pyplot as plt

#Let the constant function be f(x)=1.0
def f(x):
    return(1.0)
    
#limit of x for which we want to sample f(x)
xmin=-50.0
xmax=50.0

numpoints=128                                  #total number of points at which we want to sample f(x)
dx=(xmax-xmin)/(numpoints-1)                   #sampling rate

sampled_data=np.zeros(numpoints)
xarr=np.zeros(numpoints)

for i in range(numpoints):
    sampled_data[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
    
#DFT of the sample
nft=np.fft.fft(sampled_data, norm='ortho')

#The k array
karr=np.fft.fftfreq(numpoints, d=dx)
karr=2*np.pi*karr

#The factor due to the fact that xmin is not equal to zero
factor=np.exp(-1j*karr*xmin)

#Transforming DFT to FT
aft=dx*np.sqrt(numpoints/(2.0*np.pi))*factor*nft

plt.plot(karr,aft,'r')                     #plotting the numerical result
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'$\tilde{f}$',fontsize=16)
plt.legend()
plt.show()

print('The fourier transform of a constant function is a Dirac delta function')

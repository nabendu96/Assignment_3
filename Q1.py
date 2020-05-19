# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:00:17 2020

@author: nabendu
"""

#Problem 1
#Fourier Transform of sinc function using numpy

import numpy as np
import cmath
import matplotlib.pyplot as plt

#The given sinc function 
def f(x):
    if(x==0):
        return(1.0)
    else:
        return(np.sin(x)/x)
        
#Analytic fourier transform of sinc function is a box function    
def analytical_ft(k):
    if(abs(k)<1.0 and k>-1.0):
        return(np.sqrt(np.pi/2.0))
    else:
        return(0.0)

#limit of x for which we want to sample f(x) 
xmin=-500.0
xmax=500.0

numpoints=1024                             #total number of points at which we want to sample f(x)
dx=(xmax-xmin)/(numpoints-1)              #sampling rate 

sampled_data=np.zeros(numpoints)
xarr=np.zeros(numpoints)

#sampling f(x)
for i in range(numpoints):
    sampled_data[i]=f(xmin+i*dx)         #sampling of f(x)
    xarr[i]=xmin+i*dx                    #sample points
    
#DFT of the sample
nft=np.fft.fft(sampled_data, norm='ortho')

#The k array
karr=np.fft.fftfreq(numpoints, d=dx)
karr=2*np.pi*karr

#The factor due to the fact that xmin is not equal to zero
factor=np.exp(-1j*karr*xmin)

#Transforming DFT to FT
aft=dx*np.sqrt(numpoints/(2.0*np.pi))*factor*nft

analytical_aft=np.zeros(numpoints)

for j in range(numpoints):
    analytical_aft[j]=analytical_ft(karr[j])          #analytic solution

plt.plot(karr,aft,'.r',label=r'numerical result')                     #plotting the numerical result
plt.plot(karr,analytical_aft,'.g',label=r'analytical result')          #plotting the analytic result
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'$\tilde{f}$',fontsize=16)
plt.legend()
plt.show()

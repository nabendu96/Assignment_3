# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:07:33 2020

@author: nabendu
"""

#Problem 1
#Convolution of box function with itself

import numpy as np
from matplotlib import pyplot as plt

#the 1st function
def f1(x):
    if(abs(x)<1.0 and x>-1.0):
        return(1.0)
    else :
        return(0.0)

#the 2nd function       #in this question both are box function
def f2(x):
    if(x<1.0 and x>-1.0):
        return(1.0)
    else :
        return(0.0)
    
xmin=-5.0
xmax=5.0

numpoints=1024
dx=(xmax-xmin)/(numpoints-1)

sampled_data1=np.zeros(numpoints)
sampled_data2=np.zeros(numpoints)
xarr=np.zeros(numpoints)

#sampling the two functions
for i in range (numpoints):
    sampled_data1[i]=f1(xmin+i*dx)
    sampled_data2[i]=f2(xmin+i*dx)
    xarr[i]=xmin+i*dx

#DFT of the two sampled functions
nft1=np.fft.fft(sampled_data1,n=2*numpoints,norm='ortho')               #with zero padding
nft2=np.fft.fft(sampled_data2,n=2*numpoints,norm='ortho')               #with zero padding

#karr with zero padding
karr=np.fft.fftfreq(2*numpoints,d=dx)
karr=2*np.pi*karr

dk=karr[1]-karr[0]

#correspong x array
xarr_padding=np.fft.fftfreq(2*numpoints,d=dk)
xarr_padding=2*np.pi*xarr_padding

#factor for xmin not equal to zero 
factor=np.exp(-1j*karr*xmin)

aft1=factor*nft1
aft2=factor*nft2

#multiplying the dfts and taking inverse dft for convolution
convo_prime=np.fft.ifft(aft1*aft2,norm='ortho')
convo=dx*np.sqrt(2*numpoints)*convo_prime                #appropriate factors has to be multiplied for ft

plt.xlim(-5,5)
plt.ylim(0,2.5)
plt.plot(xarr_padding,convo,'.r',label=r'numerical convolution')       #plotting the concolution
plt.plot(xarr,sampled_data1,'g',label=r'given box function')           #plotting the box function
plt.legend()
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Sun May 17 07:45:26 2020

@author: nabendu
"""

#Problem 10
#power spectrum

import numpy as np
import matplotlib.pyplot as plt

#reading the datas 
file=open('noise.txt','r')         #the file 'noise.txt' contains the given datas
data=[]
for line in file:
    data.append(float(line))

#array of the given datas
data=np.array(data)

#total no of data points
n=len(data)
print(n)

#computing dft (without normalization)
dft=np.fft.fft(data)
#k array
karr=np.fft.fftfreq(n,d=1)

P=np.abs(dft)**2/n         #power spectrum using Periodogram estimator

#plotting the data
plt.plot(data)
plt.xlabel(r'n',fontsize=16)
plt.ylabel(r'result of $n^{th}$ measurement',fontsize=16)
plt.show()

#plotting the dfts
plt.plot(karr,dft)
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'dft',fontsize=16)
plt.show()

#plotting power spectrun
plt.plot(karr,P)
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'Power spectrum',fontsize=16)
plt.show()

#plotting the power spectrum bins
bins=10
plt.hist(P,bins) 
plt.xlabel(r'Power spectrum',fontsize=16)
plt.ylabel(r'Occurance',fontsize=16)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Mon May 18 07:34:20 2020

@author: nabendu
"""

#Problem 5
#Comparison of time taken for DFT calculation (i)directly and (ii)using numpy.fft.fft

import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

#function for estimating direct computaion time of DFT
def direct_comp_time(n):
    w_p=np.arange(n)           #sample of n numbers
    start_time1=timer()
    w_q=np.zeros(n,complex)      
    #calculating DFT directly  
    for q in range(n):
        for p in range(n):
            w_q[q]=w_q[q]+w_p[p]*np.exp(-1j*2*np.pi*q*p/n)
    w_q=w_q/np.sqrt(n)               #normalization
    end_time1=timer()
    t_direct_comp=end_time1-start_time1
    return(t_direct_comp)
    
#function for estimating computaion time for calculating DFT using numpy.fft.fft
def numpy_fft_time(n):
    w_p=np.arange(n)            #sample of n numbers
    start_time2=timer()
    w_q=np.fft.fft(w_p,norm='ortho')                #calculating DFT using numpy.fft.fft
    end_time2=timer()
    t_numpy_fft=end_time2-start_time2
    return(t_numpy_fft)
    
n=[]
direct_comp=[]
numpy_fft=[]

#varying n from 4 to 100
for i in range(4,100):
    n.append(i)
    direct_comp.append(direct_comp_time(i))  
    numpy_fft.append(numpy_fft_time(i))

plt.plot(n,direct_comp,'g',label=r'direct computation')         #plotting direct computation time as a function of n
plt.plot(n,numpy_fft,'r',label=r'using numpy.fft.fft')           #plotting computation time for calculating DFT using numpy.fft.fft as a functon of n 
plt.xlabel(r'$n$',fontsize=16)
plt.ylabel(r'$t$',fontsize=16)
plt.legend()
plt.show()

print('The time taken by direct calculation is getting larger larger with n, but numpy.fft.fft is quite fast because it uses fft technique')

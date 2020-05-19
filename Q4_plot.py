# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:52:12 2020

@author: nabendu
"""

#plotting of the numerical data obatined by running Q4.c

import numpy as np
import matplotlib.pyplot as plt

#analytical result
def analytical_ft(k):
    return(np.exp(-k*k/4.0)/np.sqrt(2.0))

file=open('Q4.txt','r')
karr=[]
aft=[]
aft_analytical=[]

for line in file:
    k,aft_data=line.split()
    karr.append(float(k))
    aft.append(float(aft_data))
    aft_analytical.append(analytical_ft(float(k)))

plt.plot(karr,aft,'.r',label=r'numerical result')    
plt.plot(karr,aft_analytical,'.g',label=r'analytical result')
plt.xlabel(r'$k$',fontsize=16)
plt.ylabel(r'$\tilde{f}$',fontsize=16)
plt.legend()
plt.show()

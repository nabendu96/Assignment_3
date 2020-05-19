# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:24:44 2020

@author: nabendu
"""
#Problem 1
#2D Fourier Transform of Gaussian function using numpy

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from pylab import rcParams
rcParams['figure.figsize'] = 5, 5

#The given Gaussian function
def f(x, y):
    return(np.exp(-x*x-y*y))
    
#limit of x & y for which we want to sample f(x,y) 
xmin=ymin=-500.0
xmax=ymax=500.0

numpoints=1024                                   #total number of points at which we want to sample f(x,y) is numpoints*numpoints
dx=dy=(xmax-xmin)/(numpoints-1)                  #sampling rate in both direction

sampled_data=np.zeros((numpoints,numpoints))
xarr=np.zeros(numpoints)
yarr=np.zeros(numpoints)

#sampling f(x,y)
for i in range(numpoints):
    for j in range(numpoints):
        sampled_data[i][j]=f(xmin+i*dx,ymin+j*dy)              #sampling of f(x,y)
        #sample points
        xarr[i]=xmin+i*dx
        yarr[j]=xmin+j*dy

#2D DFT of the sample
nft=np.fft.fft2(sampled_data, norm='ortho')

#The k_x and k_y arrays
karr_x=np.fft.fftfreq(numpoints, d=dx)
karr_y=np.fft.fftfreq(numpoints, d=dy)
karr_x=2*np.pi*karr_x
karr_y=2*np.pi*karr_y

#The factors due to the fact that xmin & ymin are not equal to zero
factor_x=np.exp(-1j*karr_x*xmin)
factor_y=np.exp(-1j*karr_y*ymin)

#Transforming DFT to FT
aft=dx*dy*(numpoints/(2.0*np.pi))*factor_x*factor_y*nft

#k-meshgrid
k_x,k_y=np.meshgrid(karr_x,karr_y)

## 3D surface_plot
fig = plt.figure()
axes = fig.gca(projection='3d')    #gca = get current axis

# surface_plot with color grading
#plotting numerical result

p=axes.plot_surface(k_x,k_y,np.abs(aft),rstride=4,cstride=4,cmap=cm.hot,linewidth=0)
axes.set_xlabel('$k_x$',fontsize=16)
axes.set_ylabel('$k_y$',fontsize=16)
axes.set_zlabel('$f_k$',fontsize=16)
plt.title('numerical result',fontsize=16)
plt.tight_layout();
plt.show()

#plotting analytical result
fig = plt.figure()
axes = fig.gca(projection='3d')
p=axes.plot_surface(k_x,k_y,0.5*np.exp(-(k_x**2+k_y**2)/4),rstride=4,cstride=4,cmap=cm.cool,linewidth=0)       #FT of a Gaussian function is also Gaussian
axes.set_xlabel('$k_x$',fontsize=16)
axes.set_ylabel('$k_y$',fontsize=16)
axes.set_zlabel('$f_k$',fontsize=16)
plt.title('analytical result',fontsize=16)
plt.tight_layout();
plt.show()

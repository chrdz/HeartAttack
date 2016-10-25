#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
import time as t
from scipy.sparse.linalg import spsolve
from function import *

Lxmin=0
Lxmax=1
Nx=40
N=Nx**2
dx=(Lxmax-Lxmin)/(Nx-1)
x=np.linspace(Lxmin,Lxmax,Nx)

tmax=400
Nt=4000
dt=tmax/Nt

Lap=-Lap_neumann_2d(dx,Nx)*dt*10**(-3)+sp.eye(N)

y0=np.array([np.zeros(N),1*np.ones(N),1*np.ones(N),np.zeros(N)],dtype=np.float64)

plt.ion()
d=t.time()
for i in range(1,Nt+1):
    un1=spsolve(Lap,-dt*(Jfi(y0[0],y0[1])+Jso(y0[0])+Jsi(y0[0],y0[2],y0[3]))+y0[0],use_umfpack=True)
    fn1=y0+dt*func_sys(y0)
    if i==10//dt:
        un1=un1.reshape(Nx,Nx)
        for i in range(Nx//2-3,Nx//2+4):
            for j in range(Nx//2-3,Nx//2+4):
                un1[i][j]=1
        un1=un1.reshape(N)
    y0=np.array([un1,fn1[1],fn1[2],fn1[3]],dtype=np.float64)
    if i%20==0:
        plotlabel="t = %1.2f ms"%(i*dt)
        plt.title(plotlabel)
        plt.pcolormesh(x,x,y0[0].reshape(Nx,Nx))
        plt.draw()
        
print(t.time()-d)
plt.show(block=True)

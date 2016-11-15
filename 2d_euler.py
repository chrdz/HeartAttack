#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve
from function import *

Dtilde=10**(-3)

Lxmin=0
Lxmax=1
Nx=100
N=Nx**2
dx=(Lxmax-Lxmin)/(Nx-1)
x=np.linspace(Lxmin,Lxmax,Nx)
X,Y=np.meshgrid(x,x)

tmax=400
Nt=1000
dt=tmax/Nt

Lap=-Lap_neumann_2d(dx,Nx)*dt*Dtilde+sp.eye(N)

y0=np.array([np.zeros(N),1*np.ones(N),1*np.ones(N),np.zeros(N)],dtype=np.float64)

#plt.ion()

for i in range(1,Nt+1):
    un1=spsolve(Lap,-dt*(Jfi(y0[0],y0[1])+Jso(y0[0])+Jsi(y0[0],y0[2],y0[3]))+y0[0],use_umfpack=True)
    fn1=y0+dt*func_sys(y0)
    y0=np.array([un1,fn1[1],fn1[2],fn1[3]],dtype=np.float64)

    if (i*dt)%2==0:
        if i*dt==10:
            #Impulsion carrée au milieu
            #un1.reshape(Nx,Nx)[Nx//2-3:Nx//2+3,Nx//2-3:Nx//2+3]=1.
            #Impulsion bande à gauche
            un1.reshape(Nx,Nx)[0:-1,0:2]=1.
            y0[0]=un1
        if i*dt==250:
            un1.reshape(Nx,Nx)[Nx//4-3:Nx//4+3,Nx//4-3:Nx//4+3]=1.
            y0[0]=un1
        plt.title("%s : t = %1.2f ms"%(var_type,i*dt))
        plt.pcolormesh(x,x,y0[0].reshape(Nx,Nx),vmin=0,vmax=1,cmap='afmhot')
        #plt.contourf(X,Y,y0[0].reshape(Nx,Nx),vmin=0,vmax=1,cmap='afmhot')
        name=str('%04d' %i)+'.pdf'
        plt.colorbar()
        plt.savefig(name)
        plt.clf()
        #plt.draw()

#plt.show(block=True)

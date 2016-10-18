#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sp
from scipy.sparse.linalg import spsolve

Lxmin=-1
Lxmax=1
Nx=800
N=Nx**2
dx=(Lxmax-Lxmin)/(Nx-1)

N=Nx**2

val=[np.ones(Nx-1),-4*np.ones(Nx),np.ones(Nx-1)]

B1=sp.diags(val,[-1,0,1],format="csr",dtype=np.float64)
B1[0,1]=2
B1[-1,-2]=2

I=sp.eye(Nx,Nx)
P1=B1+4*I

Lap=sp.kron(I,B1)+sp.kron(P1,I)
Lap=Lap_neumann_2d(Lxmin,Lxmax,Nx)
Lap=sp.eye(N,N)-Lap/dx**2

k1=3
k2=4

b=np.ones(N,dtype=np.float64)
u=np.zeros(N,dtype=np.float64)

x=np.linspace(Lxmin,Lxmax,Nx)
y=np.linspace(Lxmin,Lxmax,Nx)

X,Y=np.meshgrid(x,y)
U=np.cos(k1*np.pi*X)*np.cos(k2*np.pi*Y)
b=np.ravel((1.+(k1**2+k2**2)*np.pi**2)*U)

S=spsolve(Lap,b,use_umfpack=True)

print(max(abs(S-np.ravel(U))))

plt.pcolormesh(x,x,S.reshape(Nx,Nx), shading='flat')
plt.axis('image')
plt.show()

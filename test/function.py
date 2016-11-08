import numpy as np
import scipy.sparse as sp
from parameter import *

def heaviside(x):
    return 1*(x>0)
def vinf(u):
    return 1*(u-thetamv<0)
def taumv(u):
    return (1-heaviside(u-thetamv))*taumv1+heaviside(u-thetamv)*taumv2
def taumw(u):
    return taumw1+(taumw2-taumw1)*(1+np.tanh(kmw*(u-umw)))/2
def tauso(u):
    return tauso1+(tauso2-tauso1)*(1+np.tanh(kso*(u-uso)))/2
def taus(u):
    return (1-heaviside(u-thetaw))*taus1+heaviside(u-thetaw)*taus2
def tauo(u):
    return (1-heaviside(u-thetao))*tauo1+heaviside(u-thetao)*tauo2
def winf(u):
    return (1-heaviside(u-thetao))*(1-u/tauwinf)+heaviside(u-thetao)*wainf
def Jfi(u,v):
    return -v*heaviside(u-thetav)*(u-thetav)*(uu-u)/taufi
def Jso(u):
    return (u-uo)*(1-heaviside(u-thetaw))/tauo(u) + heaviside(u-thetaw)/tauso(u)
def Jsi(u,w,s):
    return -heaviside(u-thetaw)*w*s/tausi
def Lap_neumann_2d(dx,Nx):
    val=[np.ones(Nx-1),-4*np.ones(Nx),np.ones(Nx-1)]
    B=sp.diags(val,[-1,0,1],format="csr",dtype=np.float64)
    B[0,1]=2
    B[-1,-2]=2
    Lap=sp.kron(sp.eye(Nx),B)+sp.kron(B+4*sp.eye(Nx),sp.eye(Nx))
    return Lap/dx**2
def func_sys(y):
    v=(1-heaviside(y[0]-thetav))*(vinf(y[0])-y[1])/taumv(y[0])-heaviside(y[0]-thetav)*y[1]/taupv
    w=(1-heaviside(y[0]-thetaw))*(winf(y[0])-y[2])/taumw(y[0])-heaviside(y[0]-thetaw)*y[2]/taupw
    s=((1+np.tanh(ks*(y[0]-us)))/2-y[3])/taus(y[0])
    return np.array([y[0],v,w,s],dtype=np.float64)

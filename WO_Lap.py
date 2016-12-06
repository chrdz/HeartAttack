#!/usr/bin/env python3

from parameter import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def heaviside(x):
    return 1*(x>0)
def vinf(x):
    return 1*(x-thetamv<0)
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
def Jfi(u, v):
    return -v*heaviside(u-thetav)*(u-thetav)*(uu-u)/taufi
def Jso(u):
    return (u-uo)*(1-heaviside(u-thetaw))/tauo(u) + heaviside(u-thetaw)/tauso(u)
def Jsi(u, w, s):
    return -heaviside(u-thetaw)*w*s/tausi
def dy(y, t):

    u, v, w, s = y[0], y[1], y[2], y[3]

    du = -(Jfi(u, v) + Jso(u) + Jsi(u,w,s))
    dv = (1-heaviside(u-thetav))*(vinf(u)-v)/taumv(u)-heaviside(u-thetav)*v/taupv
    dw = (1-heaviside(u-thetaw))*(winf(u)-w)/taumw(u)-heaviside(u-thetaw)*w/taupw
    ds = ((1+np.tanh(ks*(u-us)))/2-s)/taus(u)

    return [du, dv, dw, ds]

y0 = [0.31, 1, 1, 0]
t = np.linspace(0, 300, 1000)
y = odeint(dy, y0, t)
plt.plot(t, Jfi(y[:,0],y[:,1]), t, Jso(y[:,0]), t, Jsi(y[:,0],y[:,2],y[:,3]))
plt.title("Without Laplacian")
plt.show()

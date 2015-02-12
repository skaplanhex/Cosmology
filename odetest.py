from numpy import *
from scipy.integrate import odeint
from pylab import *
import math

# seterr(all='raise')

def deriv(a,t):
    adotsqu=a*a*H0*H0*((omega_m0/(a**3))+(omega_r0/(a**4))+(omega_de0*(a**(-3.*(1.+w))))-(k/(a**2)))
    return adotsqu**(0.5)
# def deriv(y,t):
#     return array([ y[1], -omega*omega*y[0] ])

time = linspace(0,-9.7,100)
yinit = array([1.,])

H0=0.7/(9.78)

omega_m0 = 1.
omega_r0 = 0.
omega_de0 = 0.
k = 0.
w = -1.

y1 = odeint(deriv,yinit,time)
print math.isnan(y1[0][0])
print math.isnan(y1[-1][0])

omega_m0 = 2.
omega_r0 = 0.
omega_de0 = 0.
k = 1.
w = -1.

y2 = odeint(deriv,yinit,time)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.
k = -1.
w = -1.

y3 = odeint(deriv,yinit,time)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.7
k = 0.
w = -1.

y4 = odeint(deriv,yinit,time)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.
k = 0.
w = -2./3.

y5 = odeint(deriv,yinit,time)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.
k = 0.
w = -4./3.

y6 = odeint(deriv,yinit,time)

figure()
plot(time,y1[:,0])  # y[:,0] is the first column of y
plot(time,y2[:,0])
plot(time,y3[:,0])
plot(time,y4[:,0])
plot(time,y5[:,0])
plot(time,y6[:,0])
# legend()
xlabel('t relative to today (Gyr)')
ylabel('a(t)')
show()


# t = linspace(-1,0,100)
# a0=1
# res = odeint(deriv,a0,t)
# print res
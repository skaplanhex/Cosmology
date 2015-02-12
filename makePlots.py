print "Importing libraries..."
from numpy import *
from scipy.integrate import odeint
from pylab import *
import math
import ROOT
print "done."

H0=0.7/(9.78) #in units of 1/Gyr

def deriv(a,t):
    adotsqu=a*a*H0*H0*((omega_m0/(a**3))+(omega_r0/(a**4))+(omega_de0*(a**(-3.*(1.+w))))-(k/(a**2)))
    return adotsqu**(0.5)

def fixList(l):
    temp = []
    for i in range( len(l) ):
        temp.append( l[i][0] )
    return array(temp)

# first, run backward in time.

time = linspace(0,-100,1000)
yinit = array([1.,])

omega_m0 = 1.
omega_r0 = 0.
omega_de0 = 0.
k = 0.
w = -1.

y1 = odeint(deriv,yinit,time)
# print math.isnan(y1[0][0])
# print math.isnan(y1[-1][0])

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

# Now, look forward in time.  We will stitch the two together afterward

timefuture = linspace(0,100,1000)
yinit = array([1.,])

omega_m0 = 1.
omega_r0 = 0.
omega_de0 = 0.
k = 0.
w = -1.

y1future = odeint(deriv,yinit,timefuture)
# print math.isnan(y1[0][0])
# print math.isnan(y1[-1][0])

omega_m0 = 2.
omega_r0 = 0.
omega_de0 = 0.
k = 1.
w = -1.

y2future = odeint(deriv,yinit,timefuture)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.
k = -1.
w = -1.

y3future = odeint(deriv,yinit,timefuture)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.7
k = 0.
w = -1.

y4future = odeint(deriv,yinit,timefuture)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.
k = 0.
w = -2./3.

y5future = odeint(deriv,yinit,timefuture)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.
k = 0.
w = -4./3.

y6future = odeint(deriv,yinit,timefuture)

# now stitch everything together

temptime = time[::-1]
timeall = array( temptime.tolist() + timefuture.tolist() ) #concatenate time lists

#format the y's to actually be a normal list
y1fixed = fixList(y1)
y1futurefixed = fixList(y1future)
tempa1 = y1fixed[::-1]
y1all = array( tempa1.tolist() + y1futurefixed.tolist() )

y2fixed = fixList(y2)
y2futurefixed = fixList(y2future)
tempa2 = y2fixed[::-1]
y2all = array( tempa2.tolist() + y2futurefixed.tolist() )

y3fixed = fixList(y3)
y3futurefixed = fixList(y3future)
tempa3 = y3fixed[::-1]
y3all = array( tempa3.tolist() + y3futurefixed.tolist() )

y4fixed = fixList(y4)
y4futurefixed = fixList(y4future)
tempa4 = y4fixed[::-1]
y4all = array( tempa4.tolist() + y4futurefixed.tolist() )

y5fixed = fixList(y5)
y5futurefixed = fixList(y5future)
tempa5 = y5fixed[::-1]
y5all = array( tempa5.tolist() + y5futurefixed.tolist() )

y6fixed = fixList(y6)
y6futurefixed = fixList(y6future)
tempa6 = y6fixed[::-1]
y6all = array( tempa6.tolist() + y6futurefixed.tolist() )

figure()
plot(timeall,y1all)
plot(timeall,y2all)
plot(timeall,y3all)
plot(timeall,y4all)
plot(timeall,y5all)
plot(timeall,y6all)
xlabel('t relative to today (Gyr)')
ylabel('a(t)')
semilogy()
show()


# figure()
# plot(time,y1[:,0])  # y[:,0] is the first column of y
# plot(time,y2[:,0])
# plot(time,y3[:,0])
# plot(time,y4[:,0])
# plot(time,y5[:,0])
# plot(time,y6[:,0])
# plot(timefuture,y1future[:,0])  # y[:,0] is the first column of y
# plot(timefuture,y2future[:,0])
# plot(timefuture,y3future[:,0])
# plot(timefuture,y4future[:,0])
# plot(timefuture,y5future[:,0])
# plot(timefuture,y6future[:,0])
# xlim([-100,100])
# # legend()
# xlabel('t relative to today (Gyr)')
# ylabel('a(t)')
# semilogy()
# show()


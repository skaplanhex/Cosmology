print "Importing libraries..."
from numpy import *
from scipy.integrate import odeint
from scipy.optimize import curve_fit
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

def removeNans(t,y):
    ttemp=[]
    ytemp=[]
    for i in range( len(t) ):
        tCurrent = t[i]
        yCurrent = y[i]
        # print tCurrent,yCurrent
        if not math.isnan(yCurrent):
            # print "appending"
            ttemp.append( tCurrent )
            ytemp.append( yCurrent )
    return ( array(ttemp),array(ytemp) )

def fitPoly(t,k,t0,n):
    return k*((t+t0)**n)
def fitPolyDeriv(t,k,t0,n):
    return k*n*( (t+t0)**(n-1.) )
def fitExpo(t,c1,c2):
    return exp( c1+(c2*t) )
def fitExpoDeriv(t,c1,c2):
    return c2*exp( c1+(c2*t) )

def debugY(t,y):
    f = open('debug.txt','w')
    for i in range( len(t) ):
        s = str(t[i]) + " " + str(y[i]) + "\n"
        f.write(s)
    f.close()
    figure()
    plot(t,y)
    semilogy()
    # loglog()
    show()

# first, run backward in time.

time = linspace(0,-100,1000)
yinit = array([1.,])

omega_m0 = 1.
omega_r0 = 0.
omega_de0 = 0.
k = 0.
w = -1.

y1past = odeint(deriv,yinit,time)
# print math.isnan(y1[0][0])
# print math.isnan(y1[-1][0])

omega_m0 = 2.
omega_r0 = 0.
omega_de0 = 0.
k = 1.
w = -1.

y2past = odeint(deriv,yinit,time)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.
k = -1.
w = -1.

y3past = odeint(deriv,yinit,time)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.7
k = 0.
w = -1.

y4past = odeint(deriv,yinit,time)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.7
k = 0.
w = -2./3.

y5past = odeint(deriv,yinit,time)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.7
k = 0.
w = -4./3.

y6past = odeint(deriv,yinit,time)

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
omega_de0 = 0.7
k = 0.
w = -2./3.

y5future = odeint(deriv,yinit,timefuture)

omega_m0 = 0.3
omega_r0 = 0.
omega_de0 = 0.7
k = 0.
w = -4./3.

y6future = odeint(deriv,yinit,timefuture)

# now stitch everything together

temptime = time[::-1]
timeall = array( temptime.tolist() + timefuture.tolist() ) #concatenate time lists

#format the y's to actually be a normal list
y1fixed = fixList(y1past)
y1futurefixed = fixList(y1future)
tempa1 = y1fixed[::-1]
y1all = array( tempa1.tolist() + y1futurefixed.tolist() )

y2fixed = fixList(y2past)
y2futurefixed = fixList(y2future)
tempa2 = y2fixed[::-1]
y2all = array( tempa2.tolist() + y2futurefixed.tolist() )

y3fixed = fixList(y3past)
y3futurefixed = fixList(y3future)
tempa3 = y3fixed[::-1]
y3all = array( tempa3.tolist() + y3futurefixed.tolist() )

y4fixed = fixList(y4past)
y4futurefixed = fixList(y4future)
tempa4 = y4fixed[::-1]
y4all = array( tempa4.tolist() + y4futurefixed.tolist() )

y5fixed = fixList(y5past)
y5futurefixed = fixList(y5future)
tempa5 = y5fixed[::-1]
y5all = array( tempa5.tolist() + y5futurefixed.tolist() )

y6fixed = fixList(y6past)
y6futurefixed = fixList(y6future)
tempa6 = y6fixed[::-1]
y6all = array( tempa6.tolist() + y6futurefixed.tolist() )

# There are some nans in the y's we need to get rid of.  Let's do that
t1,y1 = removeNans(timeall,y1all)
t2,y2 = removeNans(timeall,y2all)
t3,y3 = removeNans(timeall,y3all)
t4,y4 = removeNans(timeall,y4all)
t5,y5 = removeNans(timeall,y5all)
t6,y6 = removeNans(timeall,y6all)

# now have timeall and yiall for i in [1,6].  Use these for the fitting!

print "Now fitting the plots!"
# fitting to function k(t+t0)^n, parameters are [k,t0,n]

p0 = [1,9.7,0.66]
popt1,pcov1 = curve_fit(fitPoly,t1,y1,p0)
print popt1
print pcov1


p0 = [0.5,9.7,0.5]
popt2,pcov2 = curve_fit(fitPoly,t2,y2,p0)
print popt2
print pcov2

# parameters from a ROOT fit
p0 = [0.0747717,13.708127540232468,1.]
# p0 = [0.1,9.7,1.]
popt3,pcov3 = curve_fit(fitPoly,t3,y3,p0)
print popt3
print pcov3

# fit for this func is exp( c1+(c2*t) )
p0 = [0.0618829,0.0598859]
popt4,pcov4 = curve_fit(fitExpo,t4,y4,p0)
print popt4
print pcov4

p0 = [1.,17.,1.5]
popt5,pcov5 = curve_fit(fitPoly,t5,y5,p0)
print popt5
print pcov5

debugY(t6,y6)

# p0 = [1.,19.,0.7]
# popt6,pcov6 = curve_fit(fitPoly,t6,y6,p0)
# print popt6
# print pcov6

# write out the a data to text files to be plotted
print "Now writing out text files!"

f1 = open('a1.txt','w')
f2 = open('a2.txt','w')
f3 = open('a3.txt','w')
f4 = open('a4.txt','w')
f5 = open('a5.txt','w')
f6 = open('a6.txt','w')


k=popt1[0]
t0=popt1[1]
n=popt1[2]
for i in range( len(t1) ):
    currentT = t1[i]
    aFromFit = fitPoly(currentT,k,t0,n)
    aDotFromFit = fitPolyDeriv(currentT,k,t0,n)
    s = str( currentT ) + " " + str( y1[i] ) + " " + str( aFromFit ) + " " + str( aDotFromFit ) + "\n"
    f1.write(s)
f1.close()

k=popt2[0]
t0=popt2[1]
n=popt2[2]
for i in range( len(t2) ):
    currentT = t2[i]
    aFromFit = fitPoly(currentT,k,t0,n)
    aDotFromFit = fitPolyDeriv(currentT,k,t0,n)
    s = str( currentT ) + " " + str( y2[i] ) + " " + str( aFromFit ) + " " + str( aDotFromFit ) + "\n"
    f2.write(s)
f2.close()

k=popt3[0]
t0=popt3[1]
n=popt3[2]
for i in range( len(t3) ):
    currentT = t3[i]
    aFromFit = fitPoly(currentT,k,t0,n)
    aDotFromFit = fitPolyDeriv(currentT,k,t0,n)
    s = str( t3[i] ) + " " + str( y3[i] ) + " " + str( aFromFit ) + " " + str( aDotFromFit ) + "\n"
    f3.write(s)
f3.close()

c1 = popt4[0]
c2 = popt4[1]
for i in range( len(t4) ):
    currentT = t4[i]
    aFromFit = fitExpo(currentT,c1,c2)
    aDotFromFit = fitExpoDeriv(currentT,c1,c2)
    s = str( t4[i] ) + " " + str( y4[i] ) + " " + str( aFromFit ) + " " + str( aDotFromFit ) + "\n"
    f4.write(s)
f4.close()

k=popt5[0]
t0=popt5[1]
n=popt5[2]
for i in range( len(t5) ):
    currentT = t5[i]
    aFromFit = fitPoly(currentT,k,t0,n)
    aDotFromFit = fitPolyDeriv(currentT,k,t0,n)
    s = str( t5[i] ) + " " + str( y5[i] ) + " " + str( aFromFit ) + " " + str( aDotFromFit ) + "\n"
    f5.write(s)
f5.close()

for i in range( len(t6) ):
    s = str( t6[i] ) + " " + str( y6[i] ) + "\n"
    f6.write(s)
f6.close()

print "Done analyzing."



# figure()
# plot(timeall,y1all)
# plot(timeall,y2all)
# plot(timeall,y3all)
# plot(timeall,y4all)
# plot(timeall,y5all)
# plot(timeall,y6all)
# xlabel('t relative to today (Gyr)')
# ylabel('a(t)')
# semilogy()
# show()


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


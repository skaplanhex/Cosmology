print "Importing ROOT, numpy, and scipy.integrate.odeint..."
from ROOT import *
import numpy as np
from scipy.integrate import odeint
print "done."

# Xn,eq as a function of temperature. It also depends on the difference between the neutron and proton masses!
def Xneq(T,mn,mp):
    temp = np.exp( (mn-mp)/T )
    return 1./(1.+temp)

# Equation 3.27 in Dodelson. Xn is the ratio of neutrons to total nuclei. x \equiv Q/T where Q \equiv mn-mp
# In the end, after using scipy.integrate.odeint, need to change from x to T (T = Q/x, so no problem) 
def dXndx(Xn,x):
    lambda_np = ( 255./(886.7*(x**5)) )*( 12. + (6.*x) + (x**2.) ) #tau_n (neutron lifetime) =886.7 sec
    Hx1 = 1.13 # 1/sec. THIS IS ALSO A FUNCTION OF Q, NOTE THIS!!! THIS SHOULD BE CALCULATED FOR EACH MODEL!!! See Dodelson (3.28)
    term1 = x*lambda_np/Hx1
    term2 = ( np.exp(-x) - Xn*(1.+np.exp(-x)) )
    return term1*term2

mn = 939.565378 #MeV
mp = 938.272046 #MeV

Q = mn - mp

temps = np.linspace(0.07,1.5,1000)
xs = Q/temps
Xninit = 0.11
Xn = odeint(dXndx,Xninit,xs)

g = TGraph(len(temps),temps,Xn)
g.SetTitle("")
g.GetXaxis().SetTitle("Temperature (MeV)")
g.GetYaxis().SetTitle("Xn")
c = TCanvas()
g.Draw("AL")

raw_input("Enter to quit: ")
print "Importing ROOT, numpy, and scipy.integrate.odeint..."
from ROOT import *
import numpy as np
from scipy.integrate import odeint
print "done."

# returns H(x=1) in units of 1/seconds
def Hx1(Q):
    G = 0.01541903619 # in natural units
    numerator = 4.*( (np.pi)**3 )*G*(Q**4)
    final = np.sqrt(numerator/45.)*np.sqrt(10.75)
    return final

def ReverseXAxis(h):
    h.GetXaxis().SetLabelOffset(999)
    h.GetXaxis().SetTickLength(0)

    # Remove the current axis
    h.GetXaxis().SetLabelOffset(999)
    h.GetXaxis().SetTickLength(0)

    # Redraw the new axis 
    gPad.Update()
    newaxis = TGaxis(gPad.GetUxmax(), 
                                gPad.GetUymin(),
                                gPad.GetUxmin(),
                                gPad.GetUymin(),
                                h.GetXaxis().GetXmin(),
                                h.GetXaxis().GetXmax(),
                                510,"-")
    newaxis.SetLabelOffset(-0.03)
    newaxis.Draw()


def ReverseYAxis(h):
   # Remove the current axis
   h.GetYaxis().SetLabelOffset(999)
   h.GetYaxis().SetTickLength(0)

   # Redraw the new axis 
   gPad.Update()
   newaxis = TGaxis(gPad.GetUxmin(), 
                                gPad.GetUymax(),
                                gPad.GetUxmin()-0.001,
                                gPad.GetUymin(),
                                h.GetYaxis().GetXmin(),
                                h.GetYaxis().GetXmax(),
                                510,"+")
   newaxis.SetLabelOffset(-0.03)
   newaxis.Draw()
    

# Xn,eq as a function of temperature. It also depends on the difference between the neutron and proton masses!
def Xneq(T,Q):
    temp = np.exp( Q/T )
    return 1./(1.+temp)

# Equation 3.27 in Dodelson. Xn is the ratio of neutrons to total nuclei. x \equiv Q/T where Q \equiv mn-mp
# In the end, after using scipy.integrate.odeint, need to change from x to T (T = Q/x, so no problem) 
def dXndx(Xn,x):
    lambda_np = ( 255./(886.7*(x**5)) )*( 12. + (6.*x) + (x**2.) ) #tau_n (neutron lifetime) =886.7 sec
    Hx1 = 1.13 # 1/sec. THIS IS ALSO A FUNCTION OF Q, NOTE THIS!!! THIS SHOULD BE CALCULATED FOR EACH MODEL!!! See Dodelson (3.28)
    term1 = (x*lambda_np)/Hx1
    term2 = ( np.exp(-x) - Xn*(1.+np.exp(-x)) )
    return term1*term2

mn = 939.565378 #MeV
mp = 938.272046 #MeV

Q = mn - mp

Tstart = 2.
Tend = 0.1
temps = np.linspace(Tstart,Tend,1000)
xs = Q/temps
Xninit = Xneq(Tstart,Q) # choose the initial Xn to be the value of Xn,eq at the starting point of the numerical calculation
Xn = odeint(dXndx,Xninit,xs)
Xn = 2.*Xn
Xn_eq = 2.*Xneq(temps,Q)

g = TGraph(len(temps),temps,Xn)
g.SetTitle("")
g.GetXaxis().SetTitle("Temperature (MeV)")
g.GetXaxis().SetTitleOffset(1.2)
g.GetYaxis().SetTitle("Fractional Abundance")
c = TCanvas()
g.Draw("AL")
geq = TGraph(len(temps),temps,Xn_eq)
geq.SetLineColor(kRed)
geq.Draw("L")
c.SetLogx()
c.SetLogy()
g.GetXaxis().SetRangeUser(Tend,Tstart)
g.GetYaxis().SetRangeUser(0.0001,1.)

leg = TLegend(.73,.32,.97,.53)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(g,"2X_{n}","L")
leg.AddEntry(geq,"2X_{n,eq}","L")
leg.Draw()

#ReverseXAxis(g)

raw_input("Enter to quit: ")
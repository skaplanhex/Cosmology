print "Importing ROOT, numpy, and scipy.integrate.odeint..."
from ROOT import *
import numpy as np
from scipy.integrate import odeint
print "done."

# gROOT.SetBatch()

# returns H(x=1) in units of 1/seconds
def Hx1(Q):
    G = 0.01541903619 # in natural units
    numerator = 4.*( (np.pi)**3 )*G*(Q**4)
    final = np.sqrt(numerator/45.)*np.sqrt(10.75)
    return final

# Xn,eq as a function of temperature. It also depends on the difference between the neutron and proton masses!
def Xneq(T,Q):
    temp = np.exp( Q/T )
    return 1./(1.+temp)

# Equation 3.27 in Dodelson. Xn is the ratio of neutrons to total nuclei. x \equiv Q/T where Q \equiv mn-mp
# In the end, after using scipy.integrate.odeint, need to change from x to T (T = Q/x, so no problem) 
def dXndxCase1(Xn,x):
    mn = 939.565378 #MeV
    mp = 938.272046 #MeV
    oneOverMassRatio = (mn/mp)**(1.5)
    lambda_np = ( 255./(886.7*(x**5)) )*( 12. + (6.*x) + (x**2.) ) #tau_n (neutron lifetime) =886.7 sec
    Hx1 = 1.13 # 1/sec. THIS IS ALSO A FUNCTION OF Q, NOTE THIS!!! THIS SHOULD BE CALCULATED FOR EACH MODEL!!! See Dodelson (3.28)
    term1 = (x*lambda_np)/Hx1
    term2 = ( np.exp(-x)*oneOverMassRatio - Xn*( 1.+ (np.exp(-x)*oneOverMassRatio) ) )
    return term1*term2

def dXndxCase2(Xn,x):
    mp = 939.565378 #MeV
    mn = 938.272046 #MeV
    oneOverMassRatio = (mn/mp)**(1.5)
    lambda_np = ( 255./(886.7*(x**5)) )*( 12. + (6.*x) + (x**2.) ) #tau_n (neutron lifetime) =886.7 sec
    Hx1 = 1.13 # 1/sec. THIS IS ALSO A FUNCTION OF Q, NOTE THIS!!! THIS SHOULD BE CALCULATED FOR EACH MODEL!!! See Dodelson (3.28)
    term1 = (x*lambda_np)/Hx1
    term2 = ( np.exp(-x)*oneOverMassRatio - Xn*( 1.+ (np.exp(-x)*oneOverMassRatio) ) )
    return term1*term2

def dXndxCase3(Xn,x):
    mn = 2.*939.565378 #MeV
    mp = 938.272046 #MeV
    oneOverMassRatio = (mn/mp)**(1.5)
    lambda_np = ( 255./(886.7*(x**5)) )*( 12. + (6.*x) + (x**2.) ) #tau_n (neutron lifetime) =886.7 sec
    Hx1 = 1.13 # 1/sec. THIS IS ALSO A FUNCTION OF Q, NOTE THIS!!! THIS SHOULD BE CALCULATED FOR EACH MODEL!!! See Dodelson (3.28)
    term1 = (x*lambda_np)/Hx1
    term2 = ( np.exp(-x)*oneOverMassRatio - Xn*( 1.+ (np.exp(-x)*oneOverMassRatio) ) )
    return term1*term2
###################################################
# Start case 1 (normal proton/neutron masses, etc.)
###################################################
mn = 939.565378 #MeV
mp = 938.272046 #MeV

Q = mn - mp

Tstart = 2.
Tend = 0.1
temps = np.linspace(Tstart,Tend,1000)
xs = Q/temps
Xninit = Xneq(Tstart,Q) # choose the initial Xn to be the value of Xn,eq at the starting point of the numerical calculation
Xn = odeint(dXndxCase1,Xninit,xs)
Xn = 2.*Xn
Xn_eq = 2.*Xneq(temps,Q)

g1 = TGraph(len(temps),temps,Xn)
g1.SetTitle("")
g1.GetXaxis().SetTitle("Temperature (MeV)")
g1.GetXaxis().SetTitleOffset(1.2)
g1.GetYaxis().SetTitle("Fractional Abundance")
c = TCanvas()
g1.Draw("AL")
geq1 = TGraph(len(temps),temps,Xn_eq)
geq1.SetLineColor(kRed)
geq1.Draw("L")
c.SetLogx()
c.SetLogy()
g1.GetXaxis().SetRangeUser(Tend,Tstart)
g1.GetYaxis().SetRangeUser(0.0001,1.)

leg = TLegend(.73,.32,.97,.53)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(g1,"2X_{n}","L")
leg.AddEntry(geq1,"2X_{n,eq}","L")
leg.Draw()

c.SaveAs("plots/Xncomp_case1.pdf")
c.Clear()

########################################
# Start Case 2 (switch mn and mp)
########################################

mp = 939.565378 #MeV
mn = 938.272046 #MeV

Q = mn - mp

Tstart = 2.
Tend = 0.1
temps = np.linspace(Tstart,Tend,1000)
xs = Q/temps
Xninit = Xneq(Tstart,Q) # choose the initial Xn to be the value of Xn,eq at the starting point of the numerical calculation
Xn = odeint(dXndxCase2,Xninit,xs)
Xn = 2.*Xn
Xn_eq = 2.*Xneq(temps,Q)

g2 = TGraph(len(temps),temps,Xn)
g2.SetTitle("")
g2.GetXaxis().SetTitle("Temperature (MeV)")
g2.GetXaxis().SetTitleOffset(1.2)
g2.GetYaxis().SetTitle("Fractional Abundance")
c = TCanvas()
g2.Draw("AL")
geq2 = TGraph(len(temps),temps,Xn_eq)
geq2.SetLineColor(kRed)
geq2.Draw("L")
# c.SetLogx()
# c.SetLogy()
g2.GetXaxis().SetRangeUser(Tend,Tstart)
g2.GetYaxis().SetRangeUser(0.0001,1.)

leg = TLegend(.73,.32,.97,.53)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(g2,"2X_{n}","L")
leg.AddEntry(geq2,"2X_{n,eq}","L")
leg.Draw()

c.SaveAs("plots/Xncomp_case2.pdf")
f = open('plots/case2.txt','w')
for i in range(len(temps)):
    f.write("%.5f %.5f %.5f\n"%(temps[i],Xn_eq[i],Xn[i]))
f.close()
c.Clear()

########################################
# Start Case 3 (double the neutron mass)
########################################

mn = 2.*939.565378 #MeV
mp = 938.272046 #MeV

Q = mn - mp

Tstart = 2.
Tend = 0.1
temps = np.linspace(Tstart,Tend,1000)
xs = Q/temps
Xninit = Xneq(Tstart,Q) # choose the initial Xn to be the value of Xn,eq at the starting point of the numerical calculation
Xn = odeint(dXndxCase3,Xninit,xs)
Xn = 2.*Xn
Xn_eq = 2.*Xneq(temps,Q)

g3 = TGraph(len(temps),temps,Xn)
g3.SetTitle("")
g3.GetXaxis().SetTitle("Temperature (MeV)")
g3.GetXaxis().SetTitleOffset(1.2)
g3.GetYaxis().SetTitle("Fractional Abundance")
c = TCanvas()
g3.Draw("AL")
geq3 = TGraph(len(temps),temps,Xn_eq)
geq3.SetLineColor(kRed)
geq3.Draw("L")
c.SetLogx()
c.SetLogy()
g3.GetXaxis().SetRangeUser(Tend,Tstart)
# g3.GetYaxis().SetRangeUser(0.0001,1.)

leg = TLegend(.73,.32,.97,.53)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(g3,"2X_{n}","L")
leg.AddEntry(geq3,"2X_{n,eq}","L")
leg.Draw()

c.SaveAs("plots/Xncomp_case3.pdf")
f = open('plots/case3.txt','w')
for i in range(len(temps)):
    f.write("%.5f %.5f %.5f\n"%(temps[i],Xn_eq[i],Xn[i]))
f.close()
# c.Clear()

raw_input("Enter to quit: ")
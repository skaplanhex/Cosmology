from ROOT import *

#a(t)=\left(6\pi G\rho_{cr}\right)^{\frac{1}{3}}t^{\frac{2}{3}}

PI=3.1415927
G=6.67e-11
H_0=70.
rho_cr=3.*(H_0**2)/(8*PI*G)

a_ein = TF1("a_ein","[0]*x^(2./3.)",0,10)
param0=((6*PI*G*rho_cr)**(1./3.))
a_ein.SetParameter(0,param0)
c = TCanvas()
a_ein.Draw()

raw_input("Enter to quit: ")
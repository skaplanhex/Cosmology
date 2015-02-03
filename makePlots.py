print "Importing ROOT..."
from ROOT import *
print "done."

gROOT.SetBatch()

PI=3.1415927
# NEED TO FIX UNITS!
G=6.67e-11
H_0=70.
rho_cr=3.*(H_0**2)/(8*PI*G)

a_ein = TF1("a_ein","[0]*x^(2./3.)",0,10)
param0=((6*PI*G*rho_cr)**(1./3.))
a_ein.SetParameter(0,param0)
a_ein.SetLineColor(kBlack)
a_ein.SetLineWidth(1)
a_ein.SetTitle("")
a_ein.GetXaxis().SetTitle("t")
a_ein.GetYaxis().SetTitle("a(t)")
a_ein.GetYaxis().SetTitleOffset(1.3)
c = TCanvas("c","",800,800)
a_ein.Draw()
c.SaveAs("ps1_plots/a_einstein.png")

c.Clear()
rho_ein = TF1("rho_ein","[0]*(1.-2.*TMath::Log(x))",0,10)
rho_ein.SetParameter(0,rho_cr)
rho_ein.SetLineColor(kBlack)
rho_ein.SetLineWidth(1)
rho_ein.SetTitle("")
rho_ein.GetXaxis().SetTitle("t")
rho_ein.GetYaxis().SetTitle("#rho(t)")
rho_ein.GetYaxis().SetTitleOffset(1.3)
rho_ein.Draw()
c.SaveAs("ps1_plots/rho_einstein.png")

# raw_input("Enter to quit: ")
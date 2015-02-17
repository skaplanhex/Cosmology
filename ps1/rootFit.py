from ROOT import *
import numpy as np

f = open("a6.txt")

t=[]
a=[]
for line in f:
    s = line.split()
    if float(s[0]) > 32.7:
        break
    t.append( float(s[0]) )
    a.append( float(s[1]) )
t = np.array(t)
a = np.array(a)

#fitfunc = TF1("fitfunc","([0]+[1]*x+[2]*x^2)/([3]+[4]*x+[5]*x^2)",-14,31)
fitfunc = TF1("fitfunc","[0]*(x+[1])^[2]",-14,32.3)
fitfunc.SetParameter(0,10)
fitfunc.SetParameter(1,15)
fitfunc.SetParameter(2,10)
# fitfunc.SetParameter(3,10)
# fitfunc.SetParameter(4,10)
# fitfunc.SetParameter(5,10)
g = TGraph(len(t),t,a)
g.Fit(fitfunc,"","",-14,32.3)
c = TCanvas("c","",800,800)
g.Draw("A*")

raw_input("Enter to quit: ")
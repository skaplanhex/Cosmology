print "importing ROOT and numpy"
from ROOT import *
import numpy as np
print "done."

gROOT.SetBatch()

f1 = open('a1.txt','r')
f2 = open('a2.txt','r')
f3 = open('a3.txt','r')
f4 = open('a4.txt','r')
f5 = open('a5.txt','r')
f6 = open('a6.txt','r')

t1 = []
a1 = []
aFromFit1 = []
aDotFromFit1 = []

t2 = []
a2 = []
aFromFit2 = []
aDotFromFit2 = []

t3 = []
a3 = []
aFromFit3 = []
aDotFromFit3 = []

t4 = []
a4 = []
aFromFit4 = []
aDotFromFit4 = []

t5 = []
a5 = []
aFromFit5 = []
aDotFromFit5 = []

t6 = []
a6 = []
aFromFit6 = []
aDotFromFit6 = []

# Loop over each file and fill the vectors

for line in f1:
    s = line.split()
    t1.append( float(s[0]) )
    a1.append( float(s[1]) )
    aFromFit1.append( float(s[2]) )
    aDotFromFit1.append( float(s[3]) )
f1.close()
t1 = np.array(t1)
a1 = np.array(a1)
aFromFit1 = np.array(aFromFit1)
aDotFromFit1 = np.array(aDotFromFit1)

for line in f2:
    s = line.split()
    t2.append( float(s[0]) )
    a2.append( float(s[1]) )
    aFromFit2.append( float(s[2]) )
    aDotFromFit2.append( float(s[3]) )
f2.close()
t2 = np.array(t2)
a2 = np.array(a2)
aFromFit2 = np.array(aFromFit2)
aDotFromFit2 = np.array(aDotFromFit2)

for line in f3:
    s = line.split()
    t3.append( float(s[0]) )
    a3.append( float(s[1]) )
    aFromFit3.append( float(s[2]) )
    aDotFromFit3.append( float(s[3]) )
f3.close()
t3 = np.array(t3)
a3 = np.array(a3)
aFromFit3 = np.array(aFromFit3)
aDotFromFit3 = np.array(aDotFromFit3)

for line in f4:
    s = line.split()
    t4.append( float(s[0]) )
    a4.append( float(s[1]) )
    aFromFit4.append( float(s[2]) )
    aDotFromFit4.append( float(s[3]) )
f4.close()
t4 = np.array(t4)
a4 = np.array(a4)
aFromFit4 = np.array(aFromFit4)
aDotFromFit4 = np.array(aDotFromFit4)

for line in f5:
    s = line.split()
    t5.append( float(s[0]) )
    a5.append( float(s[1]) )
    aFromFit5.append( float(s[2]) )
    aDotFromFit5.append( float(s[3]) )
f5.close()
t5 = np.array(t5)
a5 = np.array(a5)
aFromFit5 = np.array(aFromFit5)
aDotFromFit5 = np.array(aDotFromFit5)

for line in f6:
    s = line.split()
    if float(s[0]) > 32.7:
        break
    t6.append( float(s[0]) )
    a6.append( float(s[1]) )
f6.close()
t6 = np.array(t6)
a6 = np.array(a6)

a1plot = TGraph(len(t1),t1,a1)
a2plot = TGraph(len(t2),t2,a2)
a3plot = TGraph(len(t3),t3,a3)
a4plot = TGraph(len(t4),t4,a4)
a5plot = TGraph(len(t5),t5,a5)
a6plot = TGraph(len(t6),t6,a6)


c = TCanvas("c","",800,800)
# c.SetGridx()
# c.SetGridy()
a1plot.SetLineColor(kRed+1)
a2plot.SetLineColor(kBlue)
a3plot.SetLineColor(kGreen+2)
a4plot.SetLineColor(kBlack)
a5plot.SetLineColor(kMagenta)
a6plot.SetLineColor(kOrange+2)
a1plot.GetXaxis().SetRangeUser(-20,35)
a1plot.GetXaxis().SetTitle("t relative to today (Gyr)")
a1plot.GetYaxis().SetTitle("a(t)")
a1plot.SetTitle("")
a1plot.Draw("AL")
a2plot.Draw("L")
a3plot.Draw("L")
a4plot.Draw("L")
a5plot.Draw("L")
a6plot.Draw("L")

leg = TLegend(.23,.64,.43,.77)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.021)
leg.AddEntry(a1plot,"Einstein de-Sitter","L")
leg.AddEntry(a2plot,"Closed","L")
leg.AddEntry(a3plot,"Open","L")
leg.AddEntry(a4plot,"#Lambda_{CDM}","L")
leg.AddEntry(a5plot,"Quintessence","L")
leg.AddEntry(a6plot,"Phantom Energy","L")
leg.Draw()

c.SaveAs("ps1_plots/a1-6.pdf")

c.Clear()

h1plot = TGraph( len(t1),t1,(aDotFromFit1/aFromFit1) )
h2plot = TGraph( len(t2),t2,(aDotFromFit2/aFromFit2) )
h3plot = TGraph( len(t3),t3,(aDotFromFit3/aFromFit3) )
h4plot = TGraph( len(t4),t4,(aDotFromFit4/aFromFit4) )
h5plot = TGraph( len(t5),t5,(aDotFromFit5/aFromFit5) )

h1plot.SetLineColor(kRed+1)
h2plot.SetLineColor(kBlue)
h3plot.SetLineColor(kGreen+2)
h4plot.SetLineColor(kBlack)
h5plot.SetLineColor(kMagenta)
h1plot.GetXaxis().SetRangeUser(-15,35)
h1plot.GetXaxis().SetTitle("t relative to today (Gyr)")
h1plot.GetYaxis().SetTitle("H (Gyr^{-1})")
h1plot.GetYaxis().SetTitleOffset(1.3)
h1plot.SetTitle("")
h1plot.Draw("AL")
h2plot.Draw("L")
h3plot.Draw("L")
h4plot.Draw("L")
h5plot.Draw("L")

leg = TLegend(.58,.64,.78,.77)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.021)
leg.AddEntry(h1plot,"Einstein de-Sitter","L")
leg.AddEntry(h2plot,"Closed","L")
leg.AddEntry(h3plot,"Open","L")
leg.AddEntry(h4plot,"#Lambda_{CDM}","L")
leg.AddEntry(h5plot,"Quintessence","L")
leg.Draw()
c.SetLogy()
c.SaveAs("ps1_plots/h1-5.pdf")

c.Clear()
a6plot = TGraph(len(t6),t6,a6)
a6plot.SetLineColor(kRed+1)
# a6plot.GetXaxis().SetRangeUser(0,32.7)
a6plot.GetXaxis().SetTitle("t relative to today (Gyr)")
a6plot.GetYaxis().SetTitle("a(t)")
a6plot.GetYaxis().SetTitleOffset(1.3)
a6plot.SetTitle("")
a6plot.Draw("AL")

leg = TLegend(.55,.64,.81,.77)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.021)
leg.AddEntry(h1plot,"Phantom Energy","L")
leg.Draw()
c.SetLogy()
c.SaveAs("ps1_plots/a6.pdf")



# raw_input("Enter to quit: ")




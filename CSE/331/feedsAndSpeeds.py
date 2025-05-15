#SFM = Surface Feet per Minute
#D = Diameter
#ipm = Inches per Minute
#cpt = chip load per tooth
# nt = number of teeth
#rpm = revs/minute
#fpr = feed per rev
#doc = depth of cut
#woc = width of cut
#mrr = metal removal rate
import tkinter as tk
#write a program to determine ipm and rpm for materials

root = tk.Tk()
root.title("Speeds and Feeds")


cutterMaterials = ['','hss', 'carbide' ]
operations = ["", "contour", "pocket", "drill", "chamfer", "3D Profile"]
mats = ["", "Aluminum", 'Brass', 'Mild Steel', 'Delrin']
diameters = [.125, .250, .375, .5, 2]

'''
class Materials:
    def __init__(self, material_name, sfm):
        self.material_name = material_name
        self.sfm =  sfm

    def __str__(self):
        return f"Material Name: {self.material_name}   Speed: {self.speed}   Feed: {self.feed}"

class Cutter:
    def __init__(self, d, nt, cutterMaterial):
        self.d = d
        self.nt = nt
        self.cutterMaterial =  cutterMaterial
'''

def calcSFM(d, rpm):
    sfm =  .262 * d * rpm
    return sfm

def calcIPM(cpt, nt, rpm):
    ipm = cpt * nt * rpm
    return ipm

def calcRPM(sfm, dia):
    rpm = (3.82*sfm)/dia
    return rpm

def calcCPT(ipm, nt,rpm):
    cpt = ipm/(nt*rpm)
    return cpt

def calcFPR(ipm, rpm):
    fpr = ipm/rpm
    return fpr

def calcMRR(woc, doc, ipm):
    mrr = woc * doc * ipm
    return mrr
'''
for m in range(1, len(mats)):
    print(m, mats[m])

mat = int(input("Please choose a material: "))
print("-"*25)

for o in range(1, len(operations)):
    print(o, operations[o])

op = int(input("Please choose an operation: "))
print("-"*25)

for c in range(1, len(cutterMaterials)):
    print(c, cutterMaterials[c])

ct = int(input("Please choose an cutter type: "))
print("-"*25)
'''
global nt
global dia
#nt = int(input("How many teeth does the cutter have? ")); print()
#dia =  float(input("What is the diameter of the cutter? ")); print()


#print(f"You are {operations[op]}ing {mats[mat]} with a {nt} tooth {dia} {cutterMaterials[ct]} cutter")
#print("--" *25)
def getInput():
    nt = ntEntry.get()
    dia = diaEntry.get()
    return nt, dia

def alum():
    
    nt =  float(ntEntry.get())
    dia = float(diaEntry.get())
    sfm = 750
    cpt  = .003
    sRPM = calcRPM(sfm, dia)
    sIPM = calcIPM(cpt, nt, sRPM)

    if (sRPM > 6000):
        sRPM = sRPM/2
        sIPM = sIPM/2
    lblOutput["text"] = f" Material: Aluminum  Speed: {sRPM}     Feed: {sIPM}   Chip Load:  {cpt}    Number of Teeth: {nt}"
    #return sfm, cpt, sRPM, sIPM
def brass():
    nt =  float(ntEntry.get())
    dia = float(diaEntry.get())
    sfm = 1000
    cpt = .002
    sRPM = calcRPM(sfm, dia)
    sIPM = calcIPM(cpt, nt, sRPM)

    if sRPM > 6000:
        sRPM = sRPM/2
        sRPM = sIPM/2
    #lblOutput["text"] = "test"
    lblOutput["text"] = f"Material: Brass  Speed: {sRPM}     Feed: {sIPM}   Chip Load:  {cpt}    Number of Teeth: {nt}"
    #return sfm, cpt, sRPM, sIPM
def ms():
    nt =  float(ntEntry.get())
    dia = float(diaEntry.get())
    sfm = 100
    cpt = .0005
    sRPM = calcRPM(sfm, dia)
    sIPM = calcIPM(cpt, nt, sRPM)

    if sRPM > 6000:
        sRPM = sRPM/2
        sRPM = sIPM/2

    lblOutput["text"] = f"Material: Mild Steel Speed: {sRPM}     Feed: {sIPM}   Chip Load:  {cpt}    Number of Teeth: {nt}"
    #return sfm, cpt, sRPM, sIPM
def delrin():
    nt =  float(ntEntry.get())
    dia = float(diaEntry.get())
    sfm=200
    cpt=.003
    sRPM = calcRPM(sfm, dia)
    sIPM = calcIPM(cpt, nt, sRPM)

    if sRPM > 6000:
        sRPM = sRPM/2
        sRPM = sIPM/2
    lblOutput["text"] = f"Material: Delrin Speed: {sRPM}     Feed: {sIPM}   Chip Load:  {cpt}    Number of Teeth: {nt}"
    #return sfm, cpt, sRPM, sIPM



frameA = tk.Frame()
frameB = tk.Frame()
frameC =  tk.Frame()

lblDia = tk.Label(master=frameB, text="Diameter").pack(side=tk.LEFT)
diaEntry =  tk.Entry(master= frameB)
diaEntry.pack(side=tk.LEFT)
lblNt = tk.Label(master=frameB, text="Number of Teeth").pack(side=tk.LEFT)
ntEntry = tk.Entry(master= frameB)
ntEntry.pack(side=tk.LEFT)
lblOutput = tk.Label(master=frameC, text="OUTPUT HERE")
lblOutput.pack()

btnAl =  tk.Button(master= frameA, text="Aluminum", command=alum).pack(side=tk.LEFT)
btnBr =  tk.Button(master= frameA, text="Brass", command=brass).pack(side=tk.LEFT)
btnMS =  tk.Button(master= frameA, text="Mild Steel", command=ms).pack(side=tk.LEFT)
btnDe =  tk.Button(master= frameA, text="Delrin", command = delrin).pack(side=tk.LEFT)

frameA.pack()
frameB.pack()
frameC.pack()

root.mainloop()
'''
if(mat ==1):
    #aluminum, hss, .5
    sfm = 750
    cpt  = .003
    sRPM = calcRPM(sfm, dia)
    sIPM = calcIPM(cpt, nt, sRPM)
    
    
elif(mat == 2):
    sfm = 1000
    cpt = .002
    sRPM = calcRPM(sfm, dia)
    sIPM = calcIPM(cpt, nt, sRPM)

elif(mat == 3):
    #mild steel, hss, >.5
    sfm = 100
    cpt = .0005
    sRPM = calcRPM(sfm, dia)
    sIPM = calcIPM(cpt, nt, sRPM)
elif(mat == 4):
    #delrin, carbide, >.5
    sfm = 200
    cpt = .003
    sRPM = calcRPM(sfm, dia)
    sIPM = calcIPM(cpt, nt, sRPM)
else:
    print("Invalid material")


sRPM = calcRPM(sfm, dia)
sIPM = calcIPM(cpt, nt, sRPM)
print("Suggested settings: ")
print(f"Speed: {sRPM}     Feed: {sIPM}   Chip Load:  {cpt}    Number of Teeth: {nt}")
lblOuput["text"] = f"Speed: {sRPM}     Feed: {sIPM}   Chip Load:  {cpt}    Number of Teeth: {nt}"
'''
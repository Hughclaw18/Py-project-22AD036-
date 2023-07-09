setx = set(["motorcycle", "bike",42,13,65])
sety = set(["bike", "truck",13])
setz = set(["bike"])
print("x: ",setx)
print("y: ",sety)
print("z: ",setz,"\n")
print("Checking whether X is subset of Y...... \n")
if(setx.issubset(sety)==True):
    print("The set X is the subset of set Y \n")
else:
    print("The set X is not the subset of set Y \n")
print("Checking whether Y is subset of X...... \n")
if(sety.issubset(setx)==True):
    print("The set Y is the subset of set X\n")
else:
    print("The set Y is not the subset of set X\n")
print("Checking whether Y is subset of Z...... \n")
if(sety.issubset(setz)==True):
    print("The set Y is the subset of set Z\n")
else:
    print("The set Y is not the subset of set Z\n")
print("Checking whether Z is subset of Y...... \n")
if(setz.issubset(sety)==True):
    print("The set Z is the subset of set Y\n")
else:
    print("The set Z is not the subset of set Y\n")

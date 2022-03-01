import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

extension ={}
filename = {}
#KNOWN = 0
#print("ingresar n \n")
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    ext, mt = input().split()
    extLower = ext.lower()
    #mtLower = mt.lower()
    extension[extLower] = mt

#print(extension)

#print(extension.keys())
for i in range(q):
    fname = input()  # One file name per line.
    filename[i] = fname
    #KNOWN = 0
    if '.' in filename[i]:
        if  filename[i].split(".")[-1].lower() in extension.keys():
             index= filename[i].split(".")[-1].lower()
             print(extension[index])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")


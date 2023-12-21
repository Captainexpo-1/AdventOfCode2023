
f = open("../data/15.txt","r").read()
#f = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
#f="""HASH"""
f = f.split(",")
print(f)
"""Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256."""

a = 0
for i in f:
    t = 0
    for j in i:
        t += ord(j)
        t*=17
        t%=256
        #print(t)
    a += t
print(a)
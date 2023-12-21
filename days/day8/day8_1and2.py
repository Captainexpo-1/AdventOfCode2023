import itertools, re
import math

f = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split("\n\n")

with open("../data/eight.txt","r") as file:
    f = file.read().split("\n\n")

instructions = f[0]
a,b=f
y={}
g = []
for i in b.splitlines():
    #print(i.split(" = "))
    q,w=i.split(" = ")
    w=w.replace("(","").replace(")","").split(", ")
    # print(q)
    y[q]=[w[0],w[1]]

for i in y.keys():
    if i[-1] == "Z":
       g.append(i)

cur_instruction = "AAA"
inst_sel = 0
a = 0
b = 0
def slv(strt):
    for i,j in enumerate(itertools.cycle(instructions), 1):
        print(j)
        if j == 'R':
            strt = y[strt][1]
        else:
            strt = y[strt][0]
        if strt[-1] == "Z":
            return i
lst = []
for i in g:
    lst.append(slv(i))
print(lst)
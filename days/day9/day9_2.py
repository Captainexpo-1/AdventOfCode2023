import collections, itertools, math
f = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

with open("../data/day9.txt","r") as file:
    f = file.read()


f = f.split("\n")
result = 0
seq = [i.split(" ") for i in f]
diff = []
for idx, k in enumerate(seq):
    seq[idx] = [int(i) for i in k]
def get_till_zero(start):
    all = [start]
    while all[-1].count(0) != len(all[-1]):
        i = all[-1]
        lstdiff = i[0]
        d = []
        for j in range(len(i) - 1):
            j += 1
            d.append(i[j] - lstdiff)
            lstdiff = i[j]
        all.append(d)
    return all
def extrapolate(ls):
    for jdx,i in enumerate(ls):
        i.insert(0,None if jdx != len(ls)-1 else 0)
    print("I",ls)
    idx = len(ls)-2
    while ls[0][0] == None:
        ls[idx][0] = ls[idx][1]-ls[idx+1][0]
        idx -= 1
    print(ls)
    return ls[0][0]


for l in seq:
    result += extrapolate(get_till_zero(l))
print(result)

import time
f = open("../data/25.txt","r").read().split("\n")
fm = ("""jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr""").split("\n")
f = [i.split(":") for i in f]
conn = {}
all_wires = []
for i in f:
    a = i[1][1:].split(" ")
    conn[i[0]] = a
    b = a.copy()
    b.append(i[0])
    all_wires.extend(b)

print(conn)
all_wires = set(all_wires)
print(all_wires)

import igraph as ig # this is magic

graph = ig.Graph.ListDict(conn)

cut = graph.mincut()


print(len(cut.partition[0]) * len(cut.partition[1]))        
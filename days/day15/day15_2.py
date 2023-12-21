import json
f = open("../data/15.txt", "r").read()
#f = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
# f="""HASH"""
f = f.split(",")
#print(f)
"""Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256."""


def find_HASH(st):
    t = 0
    for j in st:
        t += ord(j)
        t *= 17
        t %= 256
    return int(t)


boxes = {i:{} for i in range(256)}
#print(boxes)

def remove(lbl):
    global boxes
    hash = find_HASH(lbl)
    boxes[hash].pop(lbl,None)
def add(lbl,fcl):
    global boxes
    hash = find_HASH(lbl)
    if lbl in boxes[hash].keys():
        boxes[hash][lbl] = fcl
        return
    boxes[hash][lbl] = fcl
def get_result():
    """
    One plus the box number of the lens in question.
    The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
    The focal length of the lens.
    """
    total = 0
    for idx,i in enumerate(boxes.keys()):
        for jdx,j in enumerate(boxes[i].keys()):
            try:
                total += (idx+1)*(jdx+1)*int(boxes[i][j])
            except:
                print(json.dumps(boxes,indent="  "),i,j)
                quit()
    return total
for i in f:
    if i.find("-")!=-1:
        lbl = i[:-1]
        fcl = "-"
    else:
        lbl = i.split("=")[0]
        fcl=i.split("=")[1]
    if fcl == "-":
        remove(lbl)
    else:
        add(lbl,fcl)
    #print(lbl, fcl)
print(get_result())

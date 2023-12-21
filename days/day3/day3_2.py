result = 0
f = open("../data/three.txt", "r").read().split("\n")
m= """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".split("\n")
def N(a):
    try:
        int(a)
    except:
        return False
    return True
def isSymbol(a):
    return not N(a) and a != "."
def getFullNum(line,j):
    r = []
    i=j
    while N(line[i]):
        r.insert(0,line[i])
        i-=1
        try: line[i]
        except: break
    i=j+1
    while N(line[i]):
        r.append(line[i])
        i+=1
        try: line[i]
        except: break
    res = ""
    for i in r: res += i
    return int(res)
def lookAround(x,y):
    nums = 1
    numCount = 0
    ul = "."*len(f[0]) if y == 0 else f[y-1]
    cl = f[y]
    ll = "."*len(f[0]) if y == len(f) else f[y+1]
    if x != 0:
        if N(cl[x-1]):
            if numCount == 2: return nums
            numCount += 1
            nums *= (n:=getFullNum(cl,x - 1))
            cl = cl.replace(f".{n}.", "."*(len(str(n))+2))
        if N(ul[x-1]):
            if numCount == 2: return nums
            numCount += 1
            nums *= (n:=getFullNum(ul, x - 1))
            ul = ul.replace(f".{n}.", "."*(len(str(n))+2))
        if N(ll[x-1]):
            if numCount == 2: return nums
            numCount += 1
            nums *= (n:=getFullNum(ll, x - 1))
            ll = ll.replace(f".{n}.", "."*(len(str(n))+2))
    if x != len(f[y][x]):
        if N(cl[x + 1]):
            if numCount == 2: return nums
            numCount += 1
            nums *= (n:=getFullNum(cl, x + 1))
            cl = cl.replace(f".{n}.", "."*(len(str(n))+2))
        if N(ul[x + 1]):
            if numCount == 2: return nums
            numCount += 1
            nums *= (n:=getFullNum(ul, x + 1))
            ul = ul.replace(f".{n}", "."*(len(str(n))+2))
        if N(ll[x + 1]):
            if numCount == 2: return nums
            numCount += 1
            nums *= (n:=getFullNum(ll, x + 1))
            ll = ll.replace(f".{n}.", "."*(len(str(n))+2))
            #print(f".{n}.", "."*(len(str(n))+2))
    if N(cl[x]):
        if numCount == 2: return nums
        numCount += 1
        nums *= (n:=getFullNum(cl, x))
    if N(ul[x]):
        if numCount == 2: return nums
        numCount += 1
        nums *= (n:=getFullNum(ul, x))
    if N(ll[x]):
        if numCount == 2: return nums
        numCount += 1
        nums *= (n:=getFullNum(ll, x))
    #print("STRT\n ",ul,"\n",cl,"\n",ll)
    return nums if numCount == 2 else 0


for idy,line in enumerate(f):
    for idx,character in enumerate(line):
        if(isSymbol(character)):
            print(character,lookAround(idx,idy))
            result += int(lookAround(idx,idy))
print(result)
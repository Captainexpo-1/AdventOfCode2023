result = 0
f = open("../data/one.txt", "r").read().split("\n")
for line in f:
    i = 0
    d1 = 0
    while i < len(line):
        try:
            d1 = int(line[i])
            print(d1)
            break
        except: pass
        i+=1
    j = len(line)
    d2 = 0
    while j >= 0:
        try:
            d2 = int(line[j])
            print(d2)
            break
        except: pass
        j-=1
    result += int(str(d1)+str(d2))
print(result)
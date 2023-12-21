f = open("../data/ten.txt","r").read()
f="""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
D=""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
f=f.split("\n")
f = [list(i) for i in f]
start_pos = []
for y,row in enumerate(f):
    for x,col in enumerate(row):
        if col == "S":
            start_pos = [y,x]
lp = start_pos
cp = start_pos
def array_has(arr,val):
    try:
        arr.index(val)
        return True
    except:
        return False

def try_remove(lst,element):
    try:
        lst.remove(element)
    except ValueError:
        # Element is not in the list, do nothing
        pass
    return lst

def get_s_pipe():
    narrow = ["|","-","L","J","7","F"]
    l = [start_pos[0],start_pos[1]-1]
    r = [start_pos[0],start_pos[1]+1]
    u = [start_pos[0]-1,start_pos[1]]
    d = [start_pos[0]+1,start_pos[1]]
    if array_has(get_next(l), start_pos):
        narrow = try_remove(narrow,"L")
        narrow = try_remove(narrow,"F")
        narrow = try_remove(narrow,"|")
    if array_has(get_next(r), start_pos):
        narrow = try_remove(narrow,"J")
        narrow = try_remove(narrow,"7")
        narrow = try_remove(narrow,"|")
    if array_has(get_next(u), start_pos):
        narrow = try_remove(narrow,"F")
        narrow = try_remove(narrow,"7")
        narrow = try_remove(narrow,"-")
    if array_has(get_next(d), start_pos):
        narrow = try_remove(narrow,"J")
        narrow = try_remove(narrow,"L")
        narrow = try_remove(narrow,"-")
    return narrow[0]
def G(n1,n2,last):
    return n2 if n1 == last else (n1 if n2 == last else n2)
def get_next(current_pos):
    current_tube = f[current_pos[0]][current_pos[1]]
    if current_tube == "|":
        return [[current_pos[0]-1,current_pos[1]],[current_pos[0]+1, current_pos[1]]]
    elif current_tube == "-":
        return [[current_pos[0], current_pos[1]+1],[current_pos[0], current_pos[1]-1]]
    elif current_tube == "L":
        return [[current_pos[0]-1, current_pos[1]],[current_pos[0], current_pos[1]+1]]
    elif current_tube == "J":
        return [[current_pos[0]-1, current_pos[1]],[current_pos[0], current_pos[1]-1]]
    elif current_tube == "7":
        return [[current_pos[0]+1, current_pos[1]],[current_pos[0], current_pos[1]-1]]
    elif current_tube == "F":
        return [[current_pos[0], current_pos[1]+1],[current_pos[0]+1, current_pos[1]]]
#while cp != start_pos:
#    print()

count = 0
distances = {}
np = cp
f[start_pos[0]][start_pos[1]] = get_s_pipe()
max = 0

while cp != start_pos or (count == 0):
    distances[str(cp)] = count
    gn = get_next(cp)
    #print(f[cp[0]][cp[1]],lp,np)
    cp, lp = G(gn[0], gn[1],lp), cp
    #print(cp,lp)
    #lp = cp

    count += 1
    #print(distances, f[lp[0]][lp[1]])
    if count % 5000 == 0: print(distances)
print(int(count / 2))

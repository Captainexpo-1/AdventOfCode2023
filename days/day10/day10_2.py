import expand_grid

f = open("../data/ten.txt", "r").read()
m = """.....
.S-7.
.|.|.
.L-J.
....."""
A = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""
m = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""
m = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""
D = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

f_2 = f.split("\n")
f_2 = [list(i) for i in f_2]
vals = list("S-7F|LJ")


def fmt_str_arr(str_arr):
    for idx, i in enumerate(str_arr):
        for idj, j in enumerate(i):
            print(j if j != "P" else f[idx][idj], end="")
        print()


f = f.split("\n")
f = [list(i) for i in f]
start_pos = []
for y, row in enumerate(f):
    for x, col in enumerate(row):
        if col == "S":
            start_pos = [y, x]
lp = start_pos
cp = start_pos


def next_to_outside(pos):
    if pos[0] == 0 or pos[1] == 0: return True
    if pos[0] == len(f_2) - 1 or pos[1] == len(f_2[0]) - 1: return True
    return False


def getNeighbors(pos):
    n = []
    try:
        if not array_has(["P", "0"], f_2[pos[0] + 1][pos[1]]): n.append([pos[0] + 1, pos[1]])
    except:
        pass
    try:
        if not array_has(["P", "0"], f_2[pos[0] - 1][pos[1]]): n.append([pos[0] - 1, pos[1]])
    except:
        pass
    try:
        if not array_has(["P", "0"], f_2[pos[0]][pos[1] + 1]): n.append([pos[0], pos[1] + 1])
    except:
        pass
    try:
        if not array_has(["P", "0"], f_2[pos[0]][pos[1] - 1]): n.append([pos[0], pos[1] - 1])
    except:
        pass
    return n


def array_has(arr, val):
    try:
        arr.index(val); return True
    except:
        return False


def try_remove(lst, element):
    try:
        lst.remove(element)
    except ValueError:
        # Element is not in the list, do nothing
        pass
    return lst


def get_s_pipe():
    narrow = ["|", "-", "L", "J", "7", "F"]
    l = [start_pos[0], start_pos[1] - 1]
    r = [start_pos[0], start_pos[1] + 1]
    u = [start_pos[0] - 1, start_pos[1]]
    d = [start_pos[0] + 1, start_pos[1]]
    if array_has(get_next(l), start_pos):
        narrow = try_remove(narrow, "L")
        narrow = try_remove(narrow, "F")
        narrow = try_remove(narrow, "|")
    if array_has(get_next(r), start_pos):
        narrow = try_remove(narrow, "J")
        narrow = try_remove(narrow, "7")
        narrow = try_remove(narrow, "|")
    if array_has(get_next(u), start_pos):
        narrow = try_remove(narrow, "F")
        narrow = try_remove(narrow, "7")
        narrow = try_remove(narrow, "-")
    if array_has(get_next(d), start_pos):
        narrow = try_remove(narrow, "J")
        narrow = try_remove(narrow, "L")
        narrow = try_remove(narrow, "-")
    return narrow[0]


def G(n1, n2, last):
    return n2 if n1 == last else (n1 if n2 == last else n2)


def get_next(current_pos):
    current_tube = f_2[current_pos[0]][current_pos[1]]
    if current_tube == "|":
        return [[current_pos[0] - 1, current_pos[1]], [current_pos[0] + 1, current_pos[1]]]
    elif current_tube == "-":
        return [[current_pos[0], current_pos[1] + 1], [current_pos[0], current_pos[1] - 1]]
    elif current_tube == "L":
        return [[current_pos[0] - 1, current_pos[1]], [current_pos[0], current_pos[1] + 1]]
    elif current_tube == "J":
        return [[current_pos[0] - 1, current_pos[1]], [current_pos[0], current_pos[1] - 1]]
    elif current_tube == "7":
        return [[current_pos[0] + 1, current_pos[1]], [current_pos[0], current_pos[1] - 1]]
    elif current_tube == "F":
        return [[current_pos[0], current_pos[1] + 1], [current_pos[0] + 1, current_pos[1]]]


# while cp != start_pos:
#    print()

count = 0
np = cp
f_2[start_pos[0]][start_pos[1]] = get_s_pipe()
max = 0

# First pass
pips = []
while cp != start_pos or (count == 0):
    gn = get_next(cp)
    #f_2[cp[0]][cp[1]]
    pips.append(cp)
    cp, lp = G(gn[0], gn[1], lp), cp
    count += 1
for idx,i in enumerate(f_2):
    for jdx,j in enumerate(i):
        if [idx,jdx] not in pips:
            f_2[idx][jdx] = "0"
# for row in f_2:
# print(''.join(row))
f_2 = expand_grid.expand_grid(f_2)

# Second pass
for idx, i in enumerate(f_2):
    for jdx, j in enumerate(i):
        f_2[idx][jdx] = "*" if j != "P" else j
        if f_2[idx][jdx] == "*":
            f_2[idx][jdx] = "0" if next_to_outside([idx, jdx]) else "*"
# Third pass
for idx, i in enumerate(f_2):
    for jdx, j in enumerate(i):
        if f_2[idx][jdx] == "*":
            f_2[idx][jdx] = "0" if next_to_outside([idx, jdx]) else "*"

# Fifth pass
changed = 1
while changed != 0:
    changed = 0
    for idx, i in enumerate(f_2):
        for jdx, j in enumerate(i):
            cur = f_2[idx][jdx]
            if cur == "0":
                for i in getNeighbors([idx, jdx]):
                    f_2[i[0]][i[1]] = "0"
                    changed += 1
    print(changed, end="\r")
# print(fmt_str_arr(f_2))
tot = 0


def grid_is_filled(g):
    return g == [
        ["*", "*", "*"],
        ["*", "*", "*"],
        ["*", "*", "*"]
    ]


def count_filled_cells(arr):
    """Count the number of 3x3 grid cells that are completely filled."""
    filled_count = 0
    for y in range(0, len(arr) - 2, 3):
        for x in range(0, len(arr[0]) - 2, 3):
            # Extract 3x3 cell
            cell = [row[x:x + 3] for row in arr[y:y + 3]]
            # Check if the cell is completely filled
            if grid_is_filled(cell):
                filled_count += 1
    return filled_count


for row in f_2:
    print(''.join(row))
    pass
# print(fmt_str_arr(f_2))
tot = 0
for i in f_2:
    for j in i:
        tot += 1 if j == "*" else 0
print(count_filled_cells(f_2))  # , tot,len(f),len(f_2))

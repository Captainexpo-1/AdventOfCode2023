import itertools,collections, sys, numpy as np
file = sys.argv[1]
use_test = True if len(sys.argv) == 3 else False
with open(f"../data/{file}.txt") as file: f = file.read()
if use_test: f = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
f = f.split("\n\n")
f = [i.split("\n") for i in f]
def transpose(matrix):
    m = [list(line) for line in matrix]
    a = np.transpose(m).tolist()
    return [list(reversed(i)) for i in a]
def get_next_static(line,ind):
    i = ind+1
    if line[ind+1] in ["#","O"]: return ind
    try:
        while not line[i+1] in ["#","O"]:
            i+=1
        return i
    except:
        return len(line)-1
def move_rocks(ln: list[chr]):
    line = ln
    for i in range(len(line)):
        if line[i] == "O":
            static = get_next_static(line,i)
            line[static] = "O"
            line[i] = "."
            static += 1
            #print("FOUND, MOVED",static)
    print(line)
    return line
def get_stress(arr):
    stress = 0
    for idx,i in enumerate(arr):
        # assuming rotated to right
        if i == "O": stress += idx+1
    #print(stress,arr)
    return stress

total = 0

for i in f:
    trn = transpose(i)
    for jdx in range(len(trn)):
        moved = trn[jdx]
        i = len(moved)-2
        while i >= 0:
            #print(i)
            if moved[i] == "O":
                static = get_next_static(moved, i)
                moved[i] = "."
                moved[static] = 'O'

            i-=1
        print(moved)
        total += get_stress(moved)
print(total)
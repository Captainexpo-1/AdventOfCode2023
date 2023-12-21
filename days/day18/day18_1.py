import AOC_Helpers as util

def tuple_add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]
f = util.read_lines("../data/18.txt")
fm = util.parse_lines("""R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""")
f = [i.split(" ")[:2] for i in f]
f = [[j[0], int(j[1])] for j in f]
current_pos = (0, 0)
positions = []
def getNeighbors(pos,grid):
    n = []
    try:
        if grid[pos[0]][pos[1]+1] == "*": return True
    except: pass
    try:
        if grid[pos[0]][pos[1] - 1] == "*": return True
    except:
        pass
    try:
        if grid[pos[0]+1][pos[1]] == "*": return True
    except:
        pass
    try:
        if grid[pos[0]-1][pos[1]] == "*": return True
    except:
        pass
    return False

for direction, steps in f:
    for _ in range(steps):
        if direction == "R":
            move = (1, 0)
        elif direction == "L":
            move = (-1, 0)
        elif direction == "U":
            move = (0, -1)
        elif direction == "D":
            move = (0, 1)
        current_pos = tuple_add(current_pos, move)
        positions.append(current_pos)

# Determine the bounds of the grid
min_x = min(positions, key=lambda x: x[0])[0]
max_x = max(positions, key=lambda x: x[0])[0]
min_y = min(positions, key=lambda x: x[1])[1]
max_y = max(positions, key=lambda x: x[1])[1]

# Create the grid
width = max_x - min_x + 1
height = max_y - min_y + 1
grid = [['.' for _ in range(width)] for _ in range(height)]

# Mark the path on the grid
for x, y in positions:
    grid[y - min_y][x - min_x] = '#'
print(grid)
# Create the string representation


changes = 1
while changes != 0:
    changes = 0
    for idx,i in enumerate(grid):
        for jdx, j in enumerate(i):
            if j == '.':
                if idx == 0 or idx == len(grid)-1 or jdx == 0 or jdx == len(grid[0])-1:
                    grid[idx][jdx] = "*"
                    changes += 1
                if j == "." and getNeighbors((idx,jdx),grid):
                    grid[idx][jdx] = "*"
                    changes += 1

print(grid)
path_str = '\n'.join([''.join(row) for row in grid])
print(path_str)
tot = 0
for j in grid:
    for k in j:
        if k in "#.": tot += 1
print(tot)
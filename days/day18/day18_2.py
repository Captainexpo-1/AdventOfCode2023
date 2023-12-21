import AOC_Helpers as util


def tuple_add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


f = util.read_lines("../data/18.txt")
m = util.parse_lines("""R 6 (#70c710)
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

dirs = "RDLU"
f = [i.split(" ")[2] for i in f]
f = [util.remove_all(chars="#()", string=i) for i in f]
f = [[dirs[int(i[-1])], int(i[:-1], 16)] for i in f]

print(f)
current_pos = (0, 0)
positions = [current_pos]
perimeter = 0
for idx, i in enumerate(f):
    # calculate bounding path length
    perimeter += i[1]
    print(perimeter)
    match i[0]:
        case "U":
            f[idx] = (0, -i[1])
        case "D":
            f[idx] = (0, i[1])
        case "L":
            f[idx] = (-i[1], 0)
        case "R":
            f[idx] = (i[1], 0)
    current_pos = tuple_add(current_pos, f[idx])
    positions.append(current_pos)

print(int(util.shoelace_area(positions) + perimeter/2+1))

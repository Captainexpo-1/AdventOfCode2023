infile = open("../data/22.txt")
#infile = open("sample.txt")

cubes = {}

for i, line in enumerate(infile):
    p0, p1 = (tuple(map(int, p.split(","))) for p in line.strip().split("~"))
    cubes[i] = (p0, p1)

gminx = min(min(x0, x1) for ((x0, _, _), (x1, _, _)) in cubes.values())
gminy = min(min(y0, y1) for ((_, y0, _), (_, y1, _)) in cubes.values())
gmaxx = max(max(x0, x1) for ((x0, _, _), (x1, _, _)) in cubes.values())
gmaxy = max(max(y0, y1) for ((_, y0, _), (_, y1, _)) in cubes.values())

grid = dict(((x,y,0), -1) for x in range(gminx, gmaxx+1) for y in range(gminy, gmaxy+1))

# lower cubes starting from the lowest ones, stopping when they collide with something
to_lower = list(range(len(cubes)))
to_lower.sort(key = lambda i: min(cubes[i][0][2], cubes[i][1][2]))
resting_on = {}
while to_lower:

    c_i = to_lower.pop(0)
    c = cubes[c_i]

    rest = set()
    rest_z = -1

    cminx = min(c[0][0], c[1][0])
    cminy = min(c[0][1], c[1][1])
    cminz = min(c[0][2], c[1][2])
    cmaxx = max(c[0][0], c[1][0])
    cmaxy = max(c[0][1], c[1][1])
    cmaxz = max(c[0][2], c[1][2])

    for ((gx, gy, gz), gi) in grid.items():
        if gx >= cminx and gx <= cmaxx and gy >= cminy and gy <= cmaxy:
            if gz > rest_z:
                rest_z = gz
                rest = set([gi])
            elif gz == rest_z:
                rest.add(gi)

    print(f"{c_i} resting on {rest}")
    resting_on[c_i] = rest

    new_z = rest_z + 1
    delta_z = new_z - cminz
    c = ((c[0][0], c[0][1], c[0][2] + delta_z),
         (c[1][0], c[1][1], c[1][2] + delta_z))
    cminz = min(c[0][2], c[1][2])
    cmaxz = max(c[0][2], c[1][2])

    for z in range(cminz, cmaxz+1):
        for y in range(cminy, cmaxy+1):
            for x in range(cminx, cmaxx+1):
                assert((x, y, z) not in grid)
                grid[(x, y, z)] = c_i

total = 0
can_disintegrate = set(range(len(cubes)))
for ri, rs in resting_on.items():
    if len(rs) == 1:
        r, = rs
        can_disintegrate.discard(r)

for c_i in range(len(cubes)):
    if c_i in can_disintegrate:
        continue
    fall = set()
    new_fall = set([c_i])
    while len(new_fall) > len(fall):
        fall.update(new_fall)
        for c_j in range(len(cubes)):
            if all(ro in new_fall for ro in resting_on[c_j]):
                new_fall.add(c_j)
    total += len(fall) - 1

print(total)


f = open("../data/five.txt", "r").read()
_ = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
ls = f.split("\n")
result = 0
seeds = [int(i) for i in ls[0][(ls[0].find(":") + 2):].split(" ")]
print(seeds)
c_map = []
maps = []
for i in ls:
    if i == "":
        maps.append(c_map)
        c_map = []
    else:
        if i.find(":") == -1:
            c_map.append(i.split(" "))
maps = maps[1:]


def in_range(n, src, length):
    if (n >= src) and (n < (src + length)):
        return True
    return False


def map_num(n, l):
    for r in l:
        # Use r[0] as source now
        # and r[1] as destination
        #print("MN",n, r[0], r[2])
        if in_range(int(n), int(r[0]), int(r[2])):
            return int(r[1]) + (int(n) - int(r[0]))
    return n

def seed_in_range(seed):
    for r in seedranges:
        start, l = r
        if (seed >= start) and (seed < (start + l)):
            return True
    return False
ranges2 = list(reversed(maps))
print(ranges2)
def get_seed(location):
    val = location
    for l in ranges2:
        # l is a list of ranges
        #print("GS",val,l)
        val = map_num(val,l)
    return val

seedranges = []
for i in range(0, len(seeds), 2):
    seedranges.append((seeds[i], seeds[i + 1]))


location = 0
while True:
    if location % 20000 == 0: print(location, end="\r", flush=True)
    seed = get_seed(location)
    if seed_in_range(seed):
        print('Part 2:', location, '(seed ' + str(seed) + ')')
        break
    location += 1

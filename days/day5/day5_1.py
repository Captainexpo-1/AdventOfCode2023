import dis
import json

f = open("../data/five.txt", "r").read()
b = """seeds: 79 14 55 13

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
print(len(seeds))
o = int(len(seeds) / 2)
off = 3 + int(len(seeds) / 2)
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
# print("STARTING")
for idx, whole in enumerate(maps):  # whole level
    destination = []
    source = []
    lengths = []
    # print(whole,cur_map)

    for ind, l in enumerate(whole):
        # print(ind, end="\r", flush=True)
        lengths.append(int(l[2]))
        c_src = int(l[0])
        c_dest = int(l[1])
        destination.append(c_dest)
        source.append(c_src)
        # print(l, len(whole), end="\r", flush=True)
    # print("\n\n", lengths, source, destination)
    # print(src)
    for jdx, i in enumerate(seeds):
        for ldx, j in enumerate(destination):
            try:
                # check if number is within range
                if i <= (j + lengths[ldx]) and i >= j:
                    offset = i - j

                    # print(seeds[jdx],"=", destination[ldx]+offset)
                    seeds[jdx] = source[ldx] + offset
                    # print("\n\n\nTEST", i, j + lengths[ldx], j, offset,source[ldx] + offset)
                    break
            except:
                pass
            # print(seeds,end="                                                \r",flush=True)
lowest = -1
for seed in seeds:
    if lowest == -1:
        lowest = seed
    elif seed < lowest:
        lowest = seed
print(lowest)
# print(maps_list)

# print(result)

# Oops, forgot to switch files when doing number two
#¯\_ (ツ)_/¯
#I guess I'll do it after the fact
import collections,itertools,numpy as np
f = open("../data/eleven.txt","r").read()

test_a = \
"""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

f = [list(i) for i in (f.split("\n") if True else test_a.split("\n"))]
result = 0

def append_rows(ls):
    m = []
    for idx,i in enumerate(ls):
        if set(i) == {"."}:
            m.append(idx)
    return m

def append_cols(ls):
    transposed_ls = np.transpose(np.array(ls))
    m = []
    for idx,i in enumerate(transposed_ls):
        if set(i) == {"."}:
            m.append(idx)
    return m

def print_str_array(arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
expansion = 999999


def get_dist_between_points(p1: tuple, p2: tuple, a1: list, a2: list) -> int:
    # Using direct calculation instead of looping through each point
    dist_x = abs(p1[0] - p2[0])
    dist_y = abs(p1[1] - p2[1])

    # Adding expansion for rows and columns
    expansion_x = sum(1 for i in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1) if i in a2) * expansion
    expansion_y = sum(1 for i in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1) if i in a1) * expansion

    return dist_x + dist_y + expansion_x + expansion_y


def get_dist_of_all_points(arr, a1, a2):
    pts = [(jdx, idx) for idx, row in enumerate(arr) for jdx, val in enumerate(row) if val == "#"]
    dist_dict = {}
    total_distance = 0

    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            # Check if the distance is already calculated
            if (pts[i], pts[j]) in dist_dict:
                dist = dist_dict[(pts[i], pts[j])]
            else:
                dist = get_dist_between_points(pts[i], pts[j], a1, a2)
                dist_dict[(pts[i], pts[j])] = dist
                dist_dict[(pts[j], pts[i])] = dist  # Symmetry, to avoid recalculating
            total_distance += dist

    return total_distance
def count_gal_in_arr(arr):
    pts = []
    for idx,i in enumerate(arr):
        for jdx, j in enumerate(i):
           if j == "#": pts.append((jdx,idx))
    return pts

a1 = append_rows(f)
a2 = append_cols(f)

print(get_dist_of_all_points(f,a1,a2))
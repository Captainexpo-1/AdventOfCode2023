from collections import deque

import AOC_Helpers as util

f = util.read_lines("../data/22.txt")
f = util.parse_lines("""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""")

f = [[[int(k) for k in j.split(",")] for j in i.split("~")] for i in f]


def sort_z_axis(brick):
    return min(int(brick[0][2]), int(brick[1][2]))


prepro = False
if not prepro:
    f.sort(key=sort_z_axis)
    print(f)
    bricks = f

if prepro: bricks = util.list_from_file("preprocess.txt")


def remove_all_duplicates(d):
    """
    Remove all instances of a value if it is a duplicate, either within its list or across different keys.

    :param d: Dictionary where values are lists of integers.
    :return: Dictionary with duplicate values removed from the lists.
    """
    value_counts = {}
    duplicates = set()

    # Count occurrences of each value across all keys
    for key in d:
        for value in d[key]:
            if value in value_counts:
                duplicates.add(value)
            else:
                value_counts[value] = True

    # Remove duplicate values from each list in the dictionary
    for key in d:
        d[key] = [value for value in d[key] if value not in duplicates]

    return d

def fall_bricks():
    changes = 1
    while changes != 0:
        changes = 0
        for idx, brick in enumerate(bricks):
            if (f := can_fall(brick, bricks))[0]:
                bricks[idx] = f[1]
                changes += 1


def can_fall(brick, all_bricks) -> tuple:
    new_pos = [[brick[0][0], brick[0][1], brick[0][2] - 1], [brick[1][0], brick[1][1], brick[1][2] - 1]]
    if new_pos[0][2] <= 0 or new_pos[1][2] <= 0:
        return False, None
    for other in all_bricks:
        if brick != other:
            if is_intersecting(new_pos, other):
                return False, None
    return True, new_pos


def is_intersecting(brick1, brick2):
    for i in range(3):
        if brick1[0][i] > brick2[1][i] or brick2[0][i] > brick1[1][i]:
            return False
    return True


if not prepro: fall_bricks()


def list_add(l1, l2):
    return [a + b for a, b in zip(l1, l2)]


def get_intersections(all_bricks):
    intersections = {}
    for idx, brick in enumerate(all_bricks):
        for jdx, other in enumerate(all_bricks):
            if idx != jdx:
                intersections[(idx, jdx)] = is_intersecting(
                    [list_add(brick[0], [0, 0, 1]), list_add(brick[1], [0, 0, 1])], other)
    return intersections


def get_direct_supporters(all_bricks):
    supporters = {}
    all_supporters = set()
    duplicate_supporters = set()

    # Initial collection of supporters
    for idx, brick in enumerate(all_bricks):
        supporters[idx] = set()
        for jdx, other in enumerate(all_bricks):
            if idx != jdx and is_intersecting([list_add(brick[0], [0, 0, 1]), list_add(brick[1], [0, 0, 1])], other):
                if jdx in all_supporters:
                    duplicate_supporters.add(jdx)
                else:
                    all_supporters.add(jdx)
                supporters[idx].add(jdx)

    # Removing duplicates from supporters
    print(supporters)
    supporters = remove_all_duplicates(supporters)
    print(supporters)
    return supporters


def get_all_supported_bricks(start_idx, all_bricks, direct_supporters):
    all_supported = set()
    eval_queue = deque([start_idx])

    while eval_queue:
        current_idx = eval_queue.popleft()
        for idx in direct_supporters[current_idx]:
            if idx not in all_supported:
                all_supported.add(idx)
                eval_queue.append(idx)

    return all_supported


def get_chain_reaction(all_bricks):
    total = 0
    direct_supporters = get_direct_supporters(all_bricks)
    for idx in range(len(all_bricks)):
        print(f"Processing: {idx / len(all_bricks) * 100:.2f}%")
        total += len(get_all_supported_bricks(idx, all_bricks, direct_supporters))
    return total


print(get_chain_reaction(bricks))

import AOC_Helpers as util

f = util.read_lines("../data/22.txt")
fm = util.parse_lines("""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""")

f = [[[int(k) for k in j.split(",")] for j in i.split("~")] for i in f]


def sort_z_axis(brick):
    return min(int(brick[0][2]), int(brick[1][2]))


f.sort(key=sort_z_axis)
print(f)
bricks = f


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


def is_intersecting(brick1: list[list[int]], brick2: list[list[int]]) -> bool:
    """
    Check if two bricks intersect.
    Each brick is represented as [start_point, end_point] where start_point and end_point
    are lists of coordinates [x, y, z].
    """
    # Unpack the start and end points of each brick
    start1, end1 = brick1
    start2, end2 = brick2

    # Check if there is a separation between the bricks on any axis
    # If there is a separation on any axis, the bricks do not intersect
    for i in range(3):  # Iterate over x, y, z axes
        if start1[i] > end2[i] or start2[i] > end1[i]:
            return False

    # If no separation is found on any axis, the bricks intersect
    return True


fall_bricks()
print(bricks)


def list_add(l1, l2):
    end = []
    if len(l1) != len(l2): raise ValueError("Lists must be of the same size")
    for i in range(len(l1)):
        end.append(l1[i] + l2[i])
    return end


def get_supporters(all_bricks):
    supp = {i: [] for i in range(len(all_bricks))}
    for idx, cur in enumerate(all_bricks):
        for jdx, other in enumerate(all_bricks):
            if cur == other: continue
            if is_intersecting([list_add(cur[0], [0, 0, 1]),list_add(cur[1], [0, 0, 1])], other):
                supp[idx].append(other)
    return supp
def remove_all_duplicates(brick_dict):
    """
    Remove all instances of a brick if it is a duplicate, either within its list or across different keys.
    Each brick is represented as [start_point, end_point].
    """
    # Count occurrences of each brick
    brick_counts = {}
    for key in brick_dict:
        for brick in brick_dict[key]:
            brick_tuple = tuple(map(tuple, brick))
            brick_counts[brick_tuple] = brick_counts.get(brick_tuple, 0) + 1

    # Remove bricks that have more than one occurrence
    for key in brick_dict:
        brick_dict[key] = [brick for brick in brick_dict[key] if brick_counts[tuple(map(tuple, brick))] == 1]

    return brick_dict




def get_desint(all_bricks: list):
    total = 0
    supporters: dict = get_supporters(all_bricks)
    print(supporters)
    supporters = remove_all_duplicates(supporters)
    print(supporters)
    for idx, i in enumerate(all_bricks):
        if len(supporters[idx]) == 0:
            total += 1
    print(total)

print(get_desint(bricks))
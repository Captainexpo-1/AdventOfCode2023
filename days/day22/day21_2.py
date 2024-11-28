# import AOC_Helpers as util

f = open("../data/22.txt", "r").read().split("\n")
f = ("""1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""").split("\n")

f = [[[int(k) for k in j.split(",")] for j in i.split("~")] for i in f]


def sort_z_axis(brick):
    return min(int(brick[0][2]), int(brick[1][2]))


pp = True
if not pp: f.sort(key=sort_z_axis)
print(f)
bricks = f


def fall_bricks(all_bricks):
    total_falls = 0
    changes = 1
    i = 0
    while changes != 0:
        changes = 0
        for idx, brick in enumerate(all_bricks):
            if i == 0: total_falls += 1
            if (f := can_fall(brick, all_bricks))[0]:
                all_bricks[idx] = f[1]
                changes += 1
        i += 1

    return total_falls, all_bricks


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


if not pp:
    _, bricks = fall_bricks(bricks)
else:
    import ast

    bricks = ast.literal_eval(open("preprocess.txt", "r").read())


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
            if is_intersecting([list_add(cur[0], [0, 0, 1]), list_add(cur[1], [0, 0, 1])], other):
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


# create graph of all bricks and their supporters
supporters = get_supporters(bricks)
# print(supporters)
# visualize graph (not igraph) of all bricks and their supporters (directional connection)
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
if False:
    G = nx.DiGraph()
    for key in supporters:
        for brick in supporters[key]:
            G.add_edge(key, bricks.index(brick))
    nx.draw(G, with_labels=True)
    plt.show()


# TODO: for every brick, find the bricks it supports directly and indirectly using BFS
def all_in_arr(arr, vals):
    for v in vals:
        if v not in arr: return False
    return True



print(bricks,supporters)
def find_all_supported(bricks, supporters):
    all_supported: dict[set] = {i: set() for i in range(len(bricks))}
    all_supported_connections: dict[set] = {i: set() for i in range(len(bricks))}

    def bfs(brick_idx):
        queue = deque([brick_idx])
        visited = set()
        while queue:

            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            for supported_brick in supporters.get(current, []):
                supported_idx = bricks.index(supported_brick)
                # Add the current brick as a connection to the supported brick
                all_supported_connections[supported_idx].add(current)
                if supported_idx not in visited:
                    all_supported[brick_idx].add(supported_idx)
                    queue.append(supported_idx)

    for idx in range(len(bricks)):
        bfs(idx)

    # Remove duplicate connections
    for brick_idx, connections in all_supported_connections.items():
        all_supported_connections[brick_idx] = set(connections)

    def get_keys_with_value(d, val):
        all_k = set()
        for i in d.keys():
            if d[i] == val or val in d[i]:
                all_k.add(i)
        return all_k

    print(all_supported)

    def get_actual_supporters(current_brick, bricks_supporting: dict[list], brick_supported_by: dict[list]):
        actual = set()
        for supported in bricks_supporting[current_brick]:
            supported_all = get_keys_with_value(bricks_supporting,supported)
            supported_all.add(current_brick)
            can = True
            for other in supported_all:
                # here other is another brick that supports the one we're currently looking at
                if other != current_brick and other not in bricks_supporting[current_brick] and current_brick not in bricks_supporting[other]:
                    can = False
                    break

            if can:
                actual.add(supported)
        return actual
    new_supported = {}
    for idx,i in enumerate(all_supported.keys()):
        print("SUPPORTERS",idx,len(all_supported.keys()))
        new_supported[i] = get_actual_supporters(i, {i: list(j) for i,j in zip(all_supported.keys(),all_supported.values())}, {i: list(j) for i,j in zip(all_supported_connections.keys(),all_supported_connections.values())})

    return new_supported, all_supported_connections


all_supported, all_supported_connections = find_all_supported(bricks, supporters)
print("All Supported:", sum(len(i) for i in all_supported.values()))
#print("All Supported Connections:", all_supported_connections)
# All Supported: {0: {1, 2, 3, 4, 5, 6}, 1: {3, 4, 5, 6}, 2: {3, 4, 5, 6}, 3: {5, 6}, 4: {5, 6}, 5: {6}, 6: set()}

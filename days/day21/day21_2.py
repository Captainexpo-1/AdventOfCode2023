import AOC_Helpers as util
import cProfile
import numpy as np

PRINT_STATS = False

f = util.read_grid("../data/21.txt")

# Additional parsing and setup
start_pos = ()
for idx, i in enumerate(f):
    for jdx, j in enumerate(i):
        if j == "S":
            f[idx][jdx] = "."
            start_pos = ((idx, jdx), (0, 0))  # (position: tuple, grid_square: tuple)

DP = {}


# Optimized solver
def optimized_fun(n, f, start_pos, DP):
    all_positions = {start_pos}
    neighbor_cache = {}

    for l in range(n):
        new_positions = set()
        for current_pos in all_positions:
            if current_pos in neighbor_cache:
                neighbors = neighbor_cache[current_pos]
            else:
                neighbors = util.get_neighbors_with_wrap_around(current_pos[0][0], current_pos[0][1], f)
                neighbor_cache[current_pos] = neighbors

            for neighbor in neighbors:
                dp_key = (current_pos, neighbor)
                if dp_key not in DP:
                    if f[neighbor[0][0]][neighbor[0][1]] == ".":
                        app = (neighbor[0], current_pos[1])
                        if neighbor[1]:
                            app = (app[0], util.tuple_add(app[1], neighbor[2]))
                        DP[dp_key] = app

                # Ensure that dp_key exists in DP before accessing it
                if dp_key in DP and DP[dp_key] not in new_positions:
                    new_positions.add(DP[dp_key])

        all_positions = new_positions

    return len(all_positions)


# Profiling and evaluation
profiler = cProfile.Profile()
profiler.enable()


def solve(x):
    """credit to u/MediocreSoftwareEng on reddit"""
    points = []
    for i in range(3):
        res = (i, optimized_fun(65 + i * 131, f, start_pos, DP))
        points.append(res)
        print(f"Solved for point {i}, result = {res[1]}")

    coefficients = np.polyfit(*zip(*points), 2)
    result = np.polyval(coefficients, x)
    return round(result)


result = solve(202300)

profiler.disable()
if PRINT_STATS: profiler.print_stats()

print("Result:", result)

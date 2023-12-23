import AOC_Helpers as util
import cProfile
f = util.read_grid("../data/21.txt")
fm = util.parse_grid("""...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""")

profiler = cProfile.Profile()
profiler.enable()

start_pos = ()
for idx, i in enumerate(f):
    for jdx, j in enumerate(i):
        if j == "S":
            f[idx][jdx] = "."
            start_pos = ((idx, jdx),(0,0)) # (position: tuple, grid_square: tuple)

all_positions: list[tuple[tuple[int, int], tuple[int, int]]] = [start_pos]

DP = {}

for i in range(50):
    new_positions = []
    for j in all_positions:
        # Retrieve neighbors with wrap-around logic
        neighbors = util.get_neighbors_with_wrap_around(j[0][0], j[0][1], f)

        for k in neighbors:
            # Use a tuple of current position and destination as the DP key
            dp_key = (j, k)
            can_do = False
            # Check if the result is already computed
            if dp_key in DP:
                app = DP[dp_key]
                #print("OFIAWIFAW")
                can_do = True
            else:
                # Compute the result as it's not in DP
                if f[k[0][0]][k[0][1]] == ".":
                    can_do = True
                    app = (k[0], j[1])
                    if k[1]:

                        app = (app[0], util.tuple_add(app[1], k[2]))
                    DP[dp_key] = app

            # Add to new positions if not already present
            if can_do and app not in new_positions:
                new_positions.append(app)

    all_positions = new_positions
    print(i)
print(len(all_positions))
profiler.disable()
profiler.print_stats()
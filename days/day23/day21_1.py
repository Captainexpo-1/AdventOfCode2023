import AOC_Helpers as util
import heapq

f = util.read_grid("../data/23.txt")
f = util.parse_grid("""#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#""")
print(f)


def longest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    longest = [0]  # Using a list to allow modification inside the nested function

    def is_valid(r, c):
        """Check if the cell is within the grid and not a wall."""
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

    def dfs(r, c, length):
        """Depth-First Search to find the longest path."""
        if (r, c) == end:
            longest[0] = max(longest[0], length)
            return

        # Mark the cell as visited
        visited.add((r, c))

        # Explore the neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc) and (nr, nc) not in visited:
                dfs(nr, nc, length + 1)

        # Unmark the cell as visited for other paths
        visited.remove((r, c))

    dfs(start[0], start[1], 0)
    return longest[0]

# y, x
a = [0, 1]
b = [1, 7]
print(f[a[0]][a[1]])
print(f[b[0]][b[1]])
# b = (1,1)
#print(a, b)
#print(f)
print(longest_path(f,a,b),longest_path(f,b,a))
for i in f: print(''.join(i))

from collections import deque
import sys
sys.setrecursionlimit(100000)

f = open("../data/24.txt","r").read().split("\n")
fm = ("""#.#####################
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
#####################.#""").split("\n")

f = [list(i) for i in f]


def longest_path_in_grid_with_path_visualization(grid, start, end, already_visited = None):
    rows, cols = len(grid), len(grid[0])
    longest_path = {"length": 0, "path": []}
    visited = set()
    def is_valid(r, c, lr,lc):
        """Check if the cell is within the grid and not a wall."""
        diff = (r-lr,c-lc)
        cur_sqr = grid[lr][lc]
        if already_visited and (r,c) in already_visited: return False
        if cur_sqr == ">":
            if diff != (0,1): return False 
        if cur_sqr == "<":
            if diff != (0,-1): return False 
        if cur_sqr == "^":
            if diff != (-1,0): return False 
        if cur_sqr == "v":
            if diff != (1,0): return False 
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

    def dfs(r, c, path):
        """Depth-First Search to find the longest path."""
        if (r, c) == end:
            if len(path) > longest_path["length"]:
                longest_path["length"] = len(path)
                longest_path["path"] = path.copy()
                longest_path["visited"] = visited
            return

        # Mark the cell as visited
        visited.add((r, c))

        # Explore the neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc, r, c) and (nr, nc) not in visited:
                path.append((nr, nc))
                dfs(nr, nc, path)
                path.pop()

        # Unmark the cell as visited for other paths
        visited.remove((r, c))

    dfs(start[0], start[1], [start])
    return longest_path

# Function to visualize the path on the grid
def visualize_path(grid, path):
    grid_with_path = [row[:] for row in grid]  # Copy the grid
    for r, c in path:
        grid_with_path[r][c] = '*'  # Mark the path

    # Convert the grid to string for display
    return '\n'.join(''.join(row) for row in grid_with_path)


# Start and end positions
start_point = (0, f[0].index("."))  # First row
end_point = (len(f) - 1, f[-1].index("."))  # Last row

# Find the longest path and visualize it
longest_path = longest_path_in_grid_with_path_visualization(f, start_point, end_point)
print(longest_path["length"]-1)
from collections import deque

f = open("../data/24.txt","r").read().split("\n")
f = ("""#.#####################
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

def longest_path_in_grid(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    longest_path_length = [0]

    def is_valid(r, c):
        """Check if the cell is within the grid and not a wall."""
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

    def dfs(r, c, length):
        """Depth-First Search to find the longest path."""
        if (r, c) == end:
            longest_path_length[0] = max(longest_path_length[0], length)
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
    return longest_path_length[0]


# Start and end positions
start_point = (0, 0)  # Top-left corner
end_point = (3, 4)    # Bottom-right corner

# Find the longest path
longest_path_in_grid(f, start_point, end_point)

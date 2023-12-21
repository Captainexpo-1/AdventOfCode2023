from heapq import heappop, heappush

# Parse the grid from a multi-line string into a list of lists of integers
grid = [
    [int(cell) for cell in row]
    for row in """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".strip().split('\n')
]

# Define movement directions: right, down, left, up
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_in_range(position, array):
    """Check if a position is within the bounds of a 2D array."""
    rows, cols = len(array), len(array[0])
    row, col = position
    return 0 <= row < rows and 0 <= col < cols

def find_path_with_constraints(min_distance, max_distance):
    """Find the path in the grid with given min and max distance constraints."""
    queue = [(0, 0, 0, -1)]  # Priority queue: cost, x, y, disallowed direction
    visited = set()
    cost_cache = {}

    while queue:
        cost, x, y, disallowed_dir = heappop(queue)

        # Check if the goal is reached
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return cost

        # Skip already visited states
        if (x, y, disallowed_dir) in visited:
            continue
        visited.add((x, y, disallowed_dir))

        # Explore all possible directions
        for dir_index in range(4):
            if dir_index == disallowed_dir or (dir_index + 2) % 4 == disallowed_dir:
                continue  # Skip the disallowed direction

            increased_cost = 0
            for dist in range(1, max_distance + 1):
                new_x = x + DIRECTIONS[dir_index][0] * dist
                new_y = y + DIRECTIONS[dir_index][1] * dist

                if is_in_range((new_x, new_y), grid):
                    increased_cost += grid[new_x][new_y]
                    if dist < min_distance:
                        continuea

                    new_cost = cost + increased_cost
                    if cost_cache.get((new_x, new_y, dir_index), float('inf')) <= new_cost:
                        continue

                    cost_cache[(new_x, new_y, dir_index)] = new_cost
                    heappush(queue, (new_cost, new_x, new_y, dir_index))

print(f"Path cost with constraints: {find_path_with_constraints(1, 3)}")

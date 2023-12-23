def count_in_2d_matrix(vals: str, arr: list[list]):
    total = 0
    for i in arr:
        for j in i:
            if j in vals:
                total += 1
    return total
def count_in_list(ls,val):
    return int(sum(1 for i in ls if i == val))
def remove_duplicates_across_keys(d):
    """
    Remove duplicate values across different keys in a dictionary,
    where each key maps to a list of bricks.
    Each brick is represented as [start_point, end_point].
    """
    # Create a set for unique bricks across all keys
    unique_bricks = set()

    for key in d:
        new_bricks = []
        for brick in d[key]:
            # Convert brick to tuple for hashing
            brick_tuple = tuple(map(tuple, brick))
            if brick_tuple not in unique_bricks:
                new_bricks.append(brick)
                unique_bricks.add(brick_tuple)

        # Update the dictionary with non-duplicate bricks
        d[key] = new_bricks

    return d

# 2. Grid and Matrix Utilities
def get_neighbors(x, y, grid):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 4-directional
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors


def get_neighbors_with_wrap_around(x, y, grid):
    directions = [(0, 1, (1,0)), (1, 0, (0,1)), (-1, 0, (0,-1)), (0, -1, (-1,0))]  # 4-directional with labels
    neighbors = []
    rows, cols = len(grid), len(grid[0])  # Dimensions of the grid

    for dx, dy, label in directions:
        nx, ny = (x + dx) % rows, (y + dy) % cols
        did_wrap_around = (nx != x + dx) or (ny != y + dy)
        wrap_side = label if did_wrap_around else None
        neighbors.append(((nx, ny), did_wrap_around, wrap_side))

    return neighbors



def print_grid(grid):
    for row in grid:
        print(''.join(str(cell) for cell in row))


def flood_fill(original_grid: list, wall_val="#", empty_val=".", use_inside: bool = False, inside_pos: tuple = (0, 0),
               fill_val="*"):
    """
    Perform a flood fill operation on a 2D grid.

    Args:
        original_grid (list): The original 2D grid represented as a list of lists.
        wall_val (str): The value representing walls in the grid.
        empty_val (str): The value representing empty spaces in the grid.
        use_inside (bool): If True, starts the flood fill from inside_pos.
        inside_pos (tuple): The starting position for flood fill if use_inside is True.
        fill_val (str): The value to fill the empty spaces with.

    Returns:
        list: The grid with the flood fill operation applied.
    """
    grid = original_grid.copy()
    if type(grid[0]) == str: grid = [list(i) for i in grid]
    changes = 1
    if use_inside:
        grid[inside_pos[0]][inside_pos[1]] = fill_val
    while changes != 0:
        changes = 0
        for idx, i in enumerate(grid):
            for jdx, j in enumerate(i):
                if j == empty_val:
                    if not use_inside and (idx == 0 or idx == len(grid) - 1 or jdx == 0 or jdx == len(grid[0]) - 1):
                        grid[idx][jdx] = fill_val
                        changes += 1
                    if j == empty_val and check_neighbors((idx, jdx), grid):
                        grid[idx][jdx] = fill_val
                        changes += 1
    return grid


def check_neighbors(pos, grid, to_check="*"):
    return to_check in get_neighbors(pos[0], pos[1], grid)


def rotate_90_degrees(matrix):
    """Rotate a 2D matrix 90 degrees clockwise."""
    return [list(row)[::-1] for row in zip(*matrix)]


def rotate_180_degrees(matrix):
    """Rotate a 2D matrix 180 degrees."""
    return [row[::-1] for row in matrix[::-1]]


def rotate_270_degrees(matrix):
    """Rotate a 2D matrix 270 degrees clockwise."""
    return [list(row) for row in zip(*matrix[::-1])]


def transpose(matrix):
    """Transpose a 2D matrix."""
    return [list(row) for row in zip(*matrix)]


def reverse_rows(matrix):
    """Reverse the rows of a 2D matrix."""
    return matrix[::-1]


def reverse_columns(matrix):
    """Reverse the columns of a 2D matrix."""
    return [row[::-1] for row in matrix]


def invert_horizontal(matrix):
    """Invert (flip) a 2D matrix horizontally."""
    return [row[::-1] for row in matrix]


def invert_vertical(matrix):
    """Invert (flip) a 2D matrix vertically."""
    return matrix[::-1]

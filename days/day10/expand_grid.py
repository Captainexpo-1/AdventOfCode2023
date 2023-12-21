def expand_character(char):
    """Expands a single character into a 3x3 block."""
    if char == '|':
        return [['.', 'P', '.'],
                ['.', 'P', '.'],
                ['.', 'P', '.']]
    elif char == '-':
        return [['.', '.', '.'],
                ['P', 'P', 'P'],
                ['.', '.', '.']]
    elif char == 'L':
        return [['.', 'P', '.'],
                ['.', 'P', 'P'],
                ['.', '.', '.']]
    elif char == 'J':
        return [['.', 'P', '.'],
                ['P', 'P', '.'],
                ['.', '.', '.']]
    elif char == '7':
        return [['.', '.', '.'],
                ['P', 'P', '.'],
                ['.', 'P', '.']]
    elif char == 'F':
        return [['.', '.', '.'],
                ['.', 'P', 'P'],
                ['.', 'P', '.']]
    else:  # For '.' and any other characters
        return [['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.']]

def expand_grid(grid):
    """Expands each character in the grid to a 3x3 block."""
    expanded_grid = []
    for row in grid:
        new_rows = [['.' for _ in range(len(row) * 3)] for _ in range(3)]
        for x, char in enumerate(row):
            expanded_char = expand_character(char)
            for dy in range(3):
                for dx in range(3):
                    new_rows[dy][x * 3 + dx] = expanded_char[dy][dx]
        expanded_grid.extend(new_rows)
    return expanded_grid
if __name__ == "__main__":
    # Example usage
    input_string = """.....
    .F-7.
    .|.|.
    .L-J.
    ....."""
    input_grid = [list(row) for row in input_string.strip().split("\n")]
    print(input_grid)
    expanded_input_grid = expand_grid(input_grid)

    # Print the expanded grid for visual confirmation
    for row in expanded_input_grid:
        print(''.join(row))

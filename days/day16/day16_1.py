# Import necessary libraries
import itertools, collections, sys, numpy as np
import cProfile

# Add this block at the beginning of your script
profiler = cProfile.Profile()
profiler.enable()
sys.setrecursionlimit(1000000)
# Get input file name from command line arguments
file = sys.argv[1]  # Retrieve the input file name from command line arguments

# Check if a test input is provided
use_test = True if len(
    sys.argv) == 3 else False  # Determine if a test input is used based on the number of command line arguments
# Read input file or use test input
with open(f"../data/{file}.txt") as file:
    f = file.read()  # Read the content of the input file
if use_test:
    f = \
r"""..|.......
..........
.|...\....
..-...\...
.....\/...
/-.......-
\........."""  # Test input if provided
f = f.split("\n")  # Split the input into lines

# Convert the input string into a 2D list
f = [list(i) for i in f]  # Convert each line into a list of characters

# Memoization dictionary
memo_dict = {}

# Function to transpose a matrix
def transpose(matrix):
    m = [list(line) for line in matrix]  # Convert each line into a list of characters
    a = np.transpose(m).tolist()  # Transpose the matrix
    return [list(reversed(i)) for i in a]  # Reverse each row

tota = 0

def total():
    global tota
    tota += 1

# Function to traverse the grid vertically
def traverse_vertical(start_pos: list, direction: int):
    cur_pos = [start_pos.copy()[0] + direction, start_pos.copy()[1]]  # Initialize the current position
    if cur_pos[0] > len(f) or cur_pos[0] < 0:
        return []
    current_square = f[cur_pos[0]][cur_pos[1]]  # Get the current square character
    passed = []  # Initialize the list to store passed positions

    # Check memoization
    if str(tuple(cur_pos))+str(direction) in memo_dict:
        print("MEMo\n")
        return memo_dict[(str(tuple(cur_pos))+str(direction))]

    while True:
        res = cur_pos.copy()  # Create a copy of the current position
        res.append("^" if direction == -1 else "v")  # Append the direction to the position
        passed.append(res)  # Add the current position to the list of passed positions
        # Check for intersections and continue traversing accordingly
        if current_square in "\\/-":
            if current_square == "\\":
                passed.extend(traverse_horizontal(cur_pos, direction))  # Continue traversing horizontally
            elif current_square == "/":
                passed.extend(traverse_horizontal(cur_pos, -direction))  # Continue traversing horizontally
            elif current_square == "-":
                passed.extend(traverse_horizontal(cur_pos, 1))  # Continue traversing horizontally
                passed.extend(traverse_horizontal(cur_pos, -1))  # Continue traversing horizontally
            break
        else:
            r = cur_pos[0] + direction  # Calculate the next row
            # Check if reached the edge of the grid
            if r >= len(f) - 1 or r <= 0:
                memo_dict[(tuple(cur_pos), direction)] = passed  # Memoize the result
                return passed  # Return the list of passed positions if reached the edge
            cur_pos[0] += direction  # Move to the next row
            current_square = f[cur_pos[0]][cur_pos[1]]  # Get the current square character
        total()
        # print(i)  # Print the counter (for debugging)
    memo_dict[str(tuple(cur_pos))+str(direction)] = passed  # Memoize the result
    return passed  # Return the list of passed positions

# Function to traverse the grid horizontally
def traverse_horizontal(start_pos: list, direction: int, init=False):
    cur_pos = [start_pos.copy()[0], start_pos.copy()[1] + direction]  # Initialize the current position
    if cur_pos[1] > len(f[1]) or cur_pos[1] < 0:
        return []
    current_square = f[cur_pos[0]][cur_pos[1]]  # Get the current square character
    passed = []  # Initialize the list to store passed positions

    # Check memoization
    if (str(tuple(cur_pos))+ str(direction)) in memo_dict:
        return memo_dict[(str(tuple(cur_pos))+str(direction))]

    while True:
        res = cur_pos.copy()  # Create a copy of the current position
        res.append("<" if direction == -1 else ">")  # Append the direction to the position
        passed.append(res)  # Add the current position to the list of passed positions
        # Check for intersections and continue traversing accordingly
        if current_square in "\\/|":
            if current_square == "\\":
                passed.extend(traverse_vertical(cur_pos, direction))  # Continue traversing vertically
            elif current_square == "/":
                passed.extend(traverse_vertical(cur_pos, -direction))  # Continue traversing vertically
            elif current_square == "|":
                passed.extend(traverse_vertical(cur_pos, -1))  # Continue traversing vertically
                passed.extend(traverse_vertical(cur_pos, 1))  # Continue traversing vertically
            break
        else:
            r = cur_pos[1] + direction  # Calculate the next column
            # Check if reached the edge of the grid
            if r >= len(f[0]) - 1 or r <= 0:
                memo_dict[(tuple(cur_pos), direction)] = passed  # Memoize the result
                return passed  # Return the list of passed positions if reached the edge
            cur_pos[1] += direction  # Move to the next column
            try:
                current_square = f[cur_pos[0]][cur_pos[1]]  # Get the current square character
            except:
                return passed
        total()
        print(tota, end="\r")
    memo_dict[(str(tuple(cur_pos))+str(direction))] = passed  # Memoize the result
    return passed  # Return the list of passed positions

# Start traversing horizontally from the top-left corner
a = traverse_horizontal([0, -1], 1, True)  # Start traversing from the top-left corner horizontally

# Remove duplicates from the list of traversed positions
b = []
for i in a:
    if i not in b:
        b.append(i)

# Print the number of unique positions
print(len(b))

# Function to visualize the grid with marked positions
def visualize_places(grid, positions):
    visualization_grid = [row.copy() for row in grid]  # Create a copy of the grid
    # Mark the positions in the visualization grid
    if positions != []:
        for position in positions:
            if f[position[0]][position[1]] == ".":
                visualization_grid[position[0]][position[1]] = position[2]

    # Print the visualization grid
    for row in visualization_grid:
        print(''.join(row))


# Print the traversed positions and visualize the grid
print(b)
visualize_places(f, b)
print()

# Remove duplicates from the list of traversed positions (ignoring direction)
b = []
for i in a:
    if i[:-1] not in b:
        b.append(i[:-1])

# Print the number of unique positions without considering direction
print(len(b))
profiler.disable()
profiler.print_stats(sort='cumulative')
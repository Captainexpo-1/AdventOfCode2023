def tilt_north(platform):
    platform = [list(row[::-1]) for row in zip(*platform)]

    for row in platform:
        for i, char in reversed(list(enumerate(row))):
            if char == "O":
                previous_index = i
                current_index = i
                reached_end = False
                while not reached_end:
                    if current_index + 1 < len(row) and row[current_index + 1] not in "#O":
                        current_index += 1
                    else:
                        reached_end = True
                row[previous_index] = "."
                row[current_index] = "O"

    return platform


def calculate_north_wall_load(platform):
    north_wall_load = 0
    current_row_num = len(platform)
    for row in platform:
        for char in row:
            if char == "O":
                north_wall_load += current_row_num
        current_row_num -= 1

    return north_wall_load


with open("../data/fourteen.txt", "r") as file:
    platform = file.read().splitlines()

seen_list = []
cycle_loop = []

for current_cycle in range(1, 1000000001):
    for _ in range(4):
        platform = tilt_north(platform)

    if platform in seen_list:
        index = seen_list.index(platform)
        cycle_loop = seen_list[index:]
        remaining_cycles = 1000000000 - current_cycle
        index_billionth = remaining_cycles % len(cycle_loop)
        print(calculate_north_wall_load(cycle_loop[index_billionth]), index_billionth, remaining_cycles, index)
        break

    seen_list.append(platform)
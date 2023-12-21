import functools
import itertools,collections, sys, re
import functools
file = sys.argv[1]
use_test = True if len(sys.argv) == 3 else False
with open(f"../data/{file}.txt") as file: f = file.read()
if use_test: f = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""
f = f.split("\n")

sep_groups = []
springs = []
ext_springs = []
for i in f:
    sep_groups.append([int(j) for j in i.split(" ")[1].split(",")])
    springs.append((i.split(" ")[0]))
    ext_springs.append("?"+i.split(" ")[0])

result = 0
print(sep_groups,springs)

# Function to count length of sequence of '#' starting from a specific index
def count_len_of_seq(seq, start):
    count = 0
    while start < len(seq) and seq[start] == "#":
        count += 1
        start += 1
    return count
def solve(dots, blocks, i, bi, current, DP):
    key = (i, bi, current)
    if key in DP:
        return DP[key]

    if i == len(dots):
        if bi == len(blocks) and current == 0:
            return 1
        elif bi == len(blocks) - 1 and blocks[bi] == current:
            return 1
        else:
            return 0

    ans = 0
    for c in ['.', '#']:
        if dots[i] == c or dots[i] == '?':
            if c == '.' and current == 0:
                ans += solve(dots, blocks, i + 1, bi, 0, DP)
            elif c == '.' and current > 0 and bi < len(blocks) and blocks[bi] == current:
                ans += solve(dots, blocks, i + 1, bi + 1, 0, DP)
            elif c == '#':
                ans += solve(dots, blocks, i + 1, bi, current + 1, DP)

    DP[key] = ans
    return ans

# Processing each spring string
for idx, i in enumerate(springs):
    DP = {}
    groups = sep_groups[idx] * 5
    s = ""
    for j in range(5):
        s += '?'
        s += i
    s += "."

    # Print the inputs for debugging
    print(f"Extended spring: {s}, Groups: {groups}")

    # Call the solve function with the extended spring
    result_this_spring = solve(s[1:], groups, 0, 0, 0, DP)

    # Print the result for this spring
    print(f"Result for spring {idx}: {result_this_spring}")

    result += result_this_spring

print(f"Total result: {result}")
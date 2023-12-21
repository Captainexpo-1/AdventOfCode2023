import itertools,collections, sys, re
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
for i in f:
    sep_groups.append([int(j) for j in i.split(" ")[1].split(",")])
    springs.append(i.split(" ")[0])

result = 0

# Function to count length of sequence of '#' starting from a specific index
def count_len_of_seq(seq, start):
    count = 0
    while start < len(seq) and seq[start] == "#":
        count += 1
        start += 1
    return count

# Processing each spring string
for idx, i in enumerate(springs):
    num_hid = i.count("?")
    combos = itertools.product(['.', '#'], repeat=num_hid)

    for combo in combos:
        temp_string = i
        for char in combo:
            temp_string = temp_string.replace('?', char, 1)

        # Find sequences of '#' and their starting indices
        hash_sequences = [m.start() for m in re.finditer("#+", temp_string)]

        # Check if the number of sequences matches and their lengths
        if len(sep_groups[idx]) == len(hash_sequences):
            valid = True
            for j, start in enumerate(hash_sequences):
                if count_len_of_seq(temp_string, start) != sep_groups[idx][j]:
                    valid = False
                    break
            if valid:
                result += 1
                print(result, idx,end="\r")
print(result)
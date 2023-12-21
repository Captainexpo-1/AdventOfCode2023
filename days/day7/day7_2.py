import itertools, collections, re
import numpy as np

f = []
use_test = False
test = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
result = 0
with open("../data/seven.txt", "r") as file:
    f = test.split("\n") if use_test else file.read().split("\n")

print(len(f))
high_low = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")
# print("HL", high_low)
bids = [i.split(" ")[1] for i in f]
hands = [i.split(" ")[0] for i in f]


def array_has(arr, val):
    try:
        return arr.index(val)
    except:
        return -1


def get_joker_permutations(counts):
    joker_count = counts[-1]
    # If no jokers, return the original counts only
    if joker_count == 0:
        return [counts]

    all_counts = []
    # Generate all combinations of replacements for jokers
    joker_replacements = list(itertools.product(high_low[:-1], repeat=joker_count))

    for replacement in joker_replacements:
        temp_counts = counts.copy()
        for card in replacement:
            temp_counts[high_low.index(card)] += 1
        # Subtract the jokers that have been replaced
        temp_counts[-1] -= joker_count
        all_counts.append(temp_counts)

    return all_counts


def find_type(counts):
    all_counts = get_joker_permutations(counts)
    best_type = -1

    for counts_perm in all_counts:
        if array_has(counts_perm, 5) != -1:
            best_type = max(best_type, 6)
        elif array_has(counts_perm, 4) != -1:
            best_type = max(best_type, 5)
        elif array_has(counts_perm, 3) != -1 and array_has(counts_perm, 2) != -1:
            best_type = max(best_type, 4)
        elif array_has(counts_perm, 3) != -1:
            best_type = max(best_type, 3)
        elif np.count_nonzero(np.array(counts_perm) == 2) == 2:
            best_type = max(best_type, 2)
        elif array_has(counts_perm, 2) != -1:
            best_type = max(best_type, 1)
        elif np.count_nonzero(np.array(counts_perm) == 1) == 5:
            best_type = max(best_type, 0)

    if best_type != -1:
        return best_type
    else:
        raise Exception("No Type Found")


types = []
for idx, i in enumerate(hands):
    counts = [0] * len(high_low)
    for j in i:
        counts[high_low.index(j)] += 1
    type = find_type(counts)
    types.append(type)


def hand_is_better(h1, h2):
    for i in range(len(h1)):
        if high_low.index(h1[i]) < high_low.index(h2[i]):
            return True
        elif high_low.index(h1[i]) > high_low.index(h2[i]):
            return False
    return False  # If hands are identical


#
def is_hands_sorted(hands, types):
    for i in range(len(hands) - 1):
        if types[i] < types[i + 1]:
            return False  # Found a hand weaker than the next one
        elif types[i] == types[i + 1] and not hand_is_better(hands[i], hands[i + 1]):
            return False  # Found two hands of the same type, but not in correct order
    return True  # All hands are in the correct order


def bubble_sort_hands(hands, types, bids):
    n = len(hands)

    while is_hands_sorted(hands, types) == False:
        swapped = False
        for i in range(1, n):
            if types[i - 1] < types[i] or (types[i - 1] == types[i] and not hand_is_better(hands[i - 1], hands[i])):
                hands[i], hands[i - 1] = hands[i - 1], hands[i]
                bids[i], bids[i - 1] = bids[i - 1], bids[i]
                types[i], types[i - 1] = types[i - 1], types[i]


bubble_sort_hands(hands, types, bids)

# Determine result
for i, l in enumerate(hands):
    print(int(bids[i]), "*", len(hands) - i, (int(bids[i]) * (len(hands) - i)))
    result += (int(bids[i]) * (len(hands) - i))

print(result)
for i in hands: print(i)

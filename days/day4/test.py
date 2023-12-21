from collections import deque

# Part 1
data = [[set([int(s) for s in n.split()]) for n in l.strip().split(":")[1].split("|")] for l in open("./../data/four.txt")]  # fmt: skip

winning_sets = {i: len(s1 & s2) for i, (s1, s2) in enumerate(data, 1)}
winning_numbers = [1 * 2 ** (s - 1) for s in winning_sets.values() if s > 0]
print(sum(winning_numbers))

# Part 2
q = deque(winning_sets.keys())

total_cards = 0
while q:
    card = q.popleft()
    total_cards += 1
    for i in range(1, winning_sets[card] + 1):
        q.appendleft(card + i)

print(total_cards)
import re

f = ""
with open("../data/six.txt", "r") as file:
    f = file.read()

f = """Time:      7  15   30
Distance:  9  40  200"""
result = 1
f = f.split("\n")
times = f[0][f[0].find(":"):]
times = re.sub(' +', ' ', times)
times = [int(i) for i in times.split(" ")[1:]]
dist = f[1][f[1].find(":"):]
dist = re.sub(' +', ' ', dist)
dist = [int(i) for i in dist.split(" ")[1:]]

for i in range(len(dist)):
    amnt = 0
    for push_seconds in range(1, times[i]):
        if push_seconds >= times[i]: continue
        dist_moved = push_seconds * (times[i] - push_seconds)

        # for j in range(times[i]-push_seconds):
        # dist_moved += push_seconds
        if dist_moved > dist[i]:
            amnt += 1
    result *= amnt
print(result)
print(times, dist)
import re
f = ""
with open("../data/six.txt","r") as file:
  f = file.read()

m = """Time:      7  15   30
Distance:  9  40  200"""
result = 1
f = f.split("\n")
times = f[0][f[0].find(":"):]
times = times.replace(" ", "")
times = int(times[1:])
dist = f[1][f[1].find(":"):]
dist = dist.replace(" ", "")
dist = int(dist[1:])

amnt = 0
for push_seconds in range(1,times):
  if push_seconds >= times: continue
  dist_moved = push_seconds * (times - push_seconds)
  amnt += 1 if dist_moved > dist else 0
  if push_seconds % 2000 == 0:
    print(amnt,push_seconds, end="\r", flush=True)
print(amnt)
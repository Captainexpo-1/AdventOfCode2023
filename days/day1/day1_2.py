f = open('../data/one.txt', "r").read().split("\n")
words = ['one', 'two', 'three.txt', 'four', 'five', 'six', 'seven', 'eight', 'nine']

result = 0
for line in f:
    d1 = 0
    for idk in range(len(line)):
        for idx, j in enumerate(words):
            idx+=1
            if line[idk:idk + len(j)] == j or line[idk] == str(idx):
                if d1 == 0:
                    d1 = idx
                d2 = idx

    result += d1*10+d2
print(result)


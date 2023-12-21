import numpy as np

with open("../data/thirteen.txt") as f:
    lines = f.read().split("\n\n")
w = \
    """#.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.
    
    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#""".split("\n\n")

lines = [line.split("\n") for line in lines]


def transpose(matrix):
    a = np.transpose(matrix).tolist()
    return [list(reversed(i)) for i in a]


def differences(a: str, b: str) -> int:
    return sum(1 for x, y in zip(a, b) if x != y)


def get_halves(str: list[str]):
    return [str[:len(str) // 2], str[len(str) // 2:]]


def find_horizontal_reflection(patt) -> int:
    length = len(patt)
    for i in range(1, length):
        num_rows = min(i, length - i)
        top = patt[i - num_rows:i]
        bottom = list(reversed(patt[i:i + num_rows]))
        if differences(''.join(top), ''.join(bottom)) == 0:
            print((''.join(top), ''.join(bottom)))
            return i


def find_vertical_reflection(p) -> int:
    patt = transpose([list(line) for line in p])
    patt = [''.join(i) for i in patt]
    return find_horizontal_reflection(patt)


def solve():
    total = 0
    for i in lines:
        hori = find_horizontal_reflection(i)
        total += (hori * 100 if hori != None else find_vertical_reflection(i))
    print(total)


solve()

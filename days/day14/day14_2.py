import itertools, collections, sys, numpy as np

file = sys.argv[1]
use_test = True if len(sys.argv) == 3 else False
with open(f"../data/{file}.txt") as file: f = file.read()
if use_test: f = \
    "O....#....\n" + \
    "O.OO#....#\n" + \
    ".....##...\n" + \
    "OO.#O....O\n" + \
    ".O.....O#.\n" + \
    "O.#..O.#.#\n" + \
    "..O..#O..O\n" + \
    ".......O..\n" + \
    "#....###..\n" + \
    "#OO..#...."
f = f.split("\n")

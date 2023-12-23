# Advent of Code Helper Functions

import os
from collections import defaultdict
from itertools import permutations, combinations


# 1. File Handling

def read_lines(file_path):
    """
    Read lines from a text file and return them as a list of strings.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list of str: A list of strings containing the lines from the file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def read_numbers(file_path):
    """
    Read numbers from a text file and return them as a list of integers.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list of int: A list of integers parsed from the lines in the file.
    """
    return [int(line) for line in read_lines(file_path)]
def replace_all_in2d(grid,rep,new):
    nn = []
    for i in grid:
        n = []
        for j in i:
            if j in rep:
                n.append(new)
            else:
                n.append(j)
        nn.append(n)
    return nn
def read_grid(file_path):
    """
    Read a grid from a text file and return it as a list of lists.

    Args:
        file_path (str): The path to the text file.

    Returns:
        list of list: A list of lists representing the grid from the file.
    """
    return [list(line) for line in read_lines(file_path)]


def parse_lines(multi_line_string):
    """
    Parse multiple lines from a string and return them as a list of strings.

    Args:
        multi_line_string (str): The input string containing multiple lines.

    Returns:
        list of str: A list of strings containing the parsed lines.
    """
    return [line.strip() for line in multi_line_string.strip().split('\n')]


def parse_numbers(multi_line_string):
    """
    Parse multiple lines from a string and return them as a list of integers.

    Args:
        multi_line_string (str): The input string containing multiple lines with integers.

    Returns:
        list of int: A list of integers parsed from the lines in the input string.
    """
    return [int(line) for line in parse_lines(multi_line_string)]


def parse_grid(multi_line_string):
    """
    Parse a grid from a string and return it as a list of lists.

    Args:
        multi_line_string (str): The input string containing the grid.

    Returns:
        list of list: A list of lists representing the parsed grid.
    """
    return [list(line) for line in parse_lines(multi_line_string)]


def remove_all(chars, string: str):
    """
    Remove all occurrences of specified characters from a string.

    Args:
        chars (str): A string containing characters to be removed.
        string (str): The input string from which characters should be removed.

    Returns:
        str: The input string with specified characters removed.
    """
    out = string
    for i in chars:
        out = out.replace(i, "")
    return out


# 3. Number Utilities

def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factors(n):
    """
    Find all factors of a number.

    Args:
        n (int): The number for which factors should be found.

    Returns:
        set: A set containing all the factors of the number.
    """
    return set(x for tup in ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0) for x in tup)


# 4. String Utilities

def hamming_distance(s1, s2):
    """
    Calculate the Hamming distance between two strings of equal length.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The Hamming distance between the two strings.
    """
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))


def string_permutations(s):
    """
    Generate all permutations of a string.

    Args:
        s (str): The input string.

    Returns:
        list of str: A list of all possible permutations of the input string.
    """
    return [''.join(p) for p in permutations(s)]




def shoelace_area(points):
    """
    Calculate the area of a polygon using the Shoelace formula.

    Parameters:
    points (list of tuples): A list of tuples representing the vertices of the polygon.

    Returns:
    float: The area of the polygon.
    """
    n = len(points)

    # Check for the minimum number of points needed to form a polygon
    if n < 3:
        raise ValueError("At least 3 points are required to form a polygon")

    area = 0
    # Sum over the vertices
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # Modulo for circular indexing
        area += x1 * y2 - y1 * x2

    return abs(area) / 2

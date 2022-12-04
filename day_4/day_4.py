import numpy as np
import pandas as pd


def split_to_range(cell):
    """Cast the string hyphen range to a python range.

    :param cell: A string annotating the range (e.g. '8-73').
    :return: The string range as a python range.
    """
    start, stop = cell.split("-")
    return range(int(start), int(stop) + 1)


def func_subset(row):
    """Check for subsets in the pair.

    :param row: Each row containing two string ranges.
    :return: True if either range is a subset of the other.
    """
    r_1 = split_to_range(row[0])
    r_2 = split_to_range(row[1])

    return set(r_1).issubset(r_2) or set(r_2).issubset(r_1)


def func_intersection(row):
    """Check for intersection in the pair.

    :param row: Each row containing two string ranges.
    :return: True if there is an intersection between the ranges.
    """
    r_1 = split_to_range(row[0])
    r_2 = split_to_range(row[1])

    return bool(set(r_1).intersection(r_2))


def part_1(arr):
    result = np.apply_along_axis(func_subset, -1, arr)
    subset_sum = result.sum()
    print(subset_sum)


def part_2(arr):
    result = np.apply_along_axis(func_intersection, -1, arr)
    intersection_sum = result.sum()
    print(intersection_sum)


def main():
    # Read the input file as a csv, then cast it to a numpy array
    df = pd.read_csv("day_4.txt", header=None)
    arr = df.values

    part_1(arr)
    part_2(arr)


if __name__ == "__main__":
    main()

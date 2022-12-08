import pandas as pd
import numpy as np
import datetime


def part_1(arr):

    visible_tree = 0

    for i in range(len(arr)):
        for j in range(len(arr)):

            value = arr[i, j]

            down = np.any(arr[i + 1:, j] >= value)
            up = np.any(arr[:i, j] >= value)
            right = np.any(arr[i, j + 1:] >= value)
            left = np.any(arr[i, :j] >= value)

            if not (down and up and right and left):
                visible_tree += 1

    print(visible_tree)


def part_2(arr):
    def custom_argmax(array, val):

        if not np.any(val <= array):
            return len(array)

        index = np.argmax(array >= val, axis=0) + 1

        return index

    highest_scenic_score = 0

    for i in range(len(arr)):
        for j in range(len(arr)):

            value = arr[i, j]

            down = custom_argmax(arr[i + 1:, j], value)
            up = custom_argmax(np.flip(arr[:i, j]), value)
            right = custom_argmax(arr[i, j + 1:], value)
            left = custom_argmax(np.flip(arr[i, :j]), value)

            scenic_score = down * up * right * left

            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    print(highest_scenic_score)


def main():
    df = pd.read_csv("day_8.txt", names=["col"], header=None)
    df = df["col"].apply(lambda x: pd.Series(list(x)))

    arr = df.values
    arr = arr.astype(int)

    part_1(arr)
    part_2(arr)


if __name__ == "__main__":
    main()

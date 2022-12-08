import pandas as pd
import numpy as np


def part_1(arr):
    count = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            value = arr[i, j]
            v1 = np.any(arr[i + 1:, j] >= value)
            v2 = np.any(arr[:i, j] >= value)
            v3 = np.any(arr[i, j + 1:] >= value)
            v4 = np.any(arr[i, :j] >= value)

            if not (v1 and v2 and v3 and v4):
                count += 1

    print(count)


def part_2(arr):
    def custom_argmax(array, val):

        if not np.any(val <= array):
            return len(array)

        index = np.argmax(array >= val, axis=0) + 1

        return index

    max_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):

            value = arr[i, j]

            v5 = custom_argmax(arr[i + 1:, j], value)
            v6 = custom_argmax(np.flip(arr[:i, j]), value)
            v7 = custom_argmax(arr[i, j + 1:], value)
            v8 = custom_argmax(np.flip(arr[i, :j]), value)

            zum = v5 * v6 * v7 * v8

            if zum > max_sum:
                max_sum = zum

    print(max_sum)


def main():
    df = pd.read_csv("day_8.txt", names=["col"], header=None)
    df = df["col"].apply(lambda x: pd.Series(list(x)))

    arr = df.values
    arr = arr.astype(int)

    part_1(arr)
    part_2(arr)


if __name__ == "__main__":
    main()

import pandas as pd
from collections import Counter


def calc(inp, unqiue_length):
    for i in range(len(inp)):
        s = inp[i: i + unqiue_length]

        length = len(Counter(s))

        if length == unqiue_length:
            print(i + unqiue_length)
            return


def main():
    inp = pd.read_csv("day_6.txt", header=None).values[0, 0]
    calc(inp, 4)
    calc(inp, 14)


if __name__ == "__main__":
    main()

import pandas as pd


def calc(inp, unqiue_length):
    """Find first string with unique characters of length unique_length in inp.

    :param inp: The day_9.txt string.
    :param unqiue_length: Length of unique characters to identify.
    :return: None, used to exit function.
    """
    for i in range(len(inp)):

        # Extract string of length unique_length
        s = inp[i: i + unqiue_length]

        # Check if all characters in the string is unique
        if len(set(s)) == unqiue_length:
            print(i + unqiue_length)
            return


def main():
    # Read as dataframe and boil it down to the single string
    inp = pd.read_csv("day_6.txt", header=None).values[0, 0]
    calc(inp, unqiue_length=4)
    calc(inp, unqiue_length=14)


if __name__ == "__main__":
    main()

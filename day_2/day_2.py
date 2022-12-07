import pandas as pd
import numpy as np


def calc_score(df):
    """Calculate the score where both columns contain A, B and C.

    :param df: A dataframe where the first column is the opponents choice, and the second is yours.
    """
    picks = df["you"].value_counts()
    picks["B"] = picks["B"] * 2
    picks["C"] = picks["C"] * 3
    pick_score = sum(picks)

    draws = df[df["opponent"] == df["you"]]

    wins = df[(((df["you"] == "A") & (df["opponent"] == "C")) |
               ((df["you"] == "B") & (df["opponent"] == "A")) |
               ((df["you"] == "C") & (df["opponent"] == "B")))]

    draw_score = len(draws.index) * 3
    win_score = len(wins.index) * 6

    print(pick_score + draw_score + win_score)


def part_1(df):
    # Rename so both columns have the same format
    df = df.replace({"you": {"X": "A", "Y": "B", "Z": "C"}})
    calc_score(df)


def part_2(df):
    # Encode the choice of 'you' column such that Y is draw, Z is a win, and X is a loss
    df["you"] = np.where(df["you"] == "Y", df["opponent"], df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "A")), "B", df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "B")), "C", df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "C")), "A", df["you"])

    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "A")), "C", df["you"])
    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "B")), "A", df["you"])
    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "C")), "B", df["you"])

    calc_score(df)


def main():
    # Read the input file with two columns, one for each 'player'
    df = pd.read_csv("day_2.txt", sep=" ", header=None, names=["opponent", "you"])

    part_1(df)
    part_1(df)


if __name__ == "__main__":
    main()

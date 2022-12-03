import pandas as pd
import numpy as np


def calc_score(df):
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

    total_score = pick_score + draw_score + win_score
    print(total_score)


def part_2(df):
    df["you"] = np.where(df["you"] == "Y", df["opponent"], df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "A")), "B", df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "B")), "C", df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "C")), "A", df["you"])

    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "A")), "C", df["you"])
    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "B")), "A", df["you"])
    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "C")), "B", df["you"])

    calc_score(df)


def part_1(df):
    df = df.replace({"you": {"X": "A", "Y": "B", "Z": "C"}})
    calc_score(df)


def main():
    df = pd.read_csv("day_2_input.csv", sep=" ", header=None, names=["opponent", "you"])
    part_1(df)
    part_2(df)


if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np

# A, X = ROCK (1 pts)
# B, Y = PAPER (2 pts)
# C, Z = SCISSORS (3 pts)

# A -> A = 3
# B -> B = 3
# C -> C = 3

# A -> B = 0
# A -> C = 6
# B -> C = 6

# X = LOSS
# Y = DRAW
# Z = WIN


def enc(df):
    df["you"] = np.where(df["you"] == "Y", df["opponent"], df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "A")), "B", df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "B")), "C", df["you"])
    df["you"] = np.where(((df["you"] == "Z") & (df["opponent"] == "C")), "A", df["you"])

    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "A")), "C", df["you"])
    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "B")), "A", df["you"])
    df["you"] = np.where(((df["you"] == "X") & (df["opponent"] == "C")), "B", df["you"])

    return df


df = pd.read_csv("day_2_input.csv", sep=" ", header=None, names=["opponent", "you"])
df = enc(df)
#df = df.replace({"you": {"X": "A", "Y": "B", "Z": "C"}})

picks = df["you"].value_counts()
picks["B"] = picks["B"] * 2
picks["C"] = picks["C"] * 3
pick_score = sum(picks)

draws = df[df["opponent"] == df["you"]]

wins = df[(((df["you"] == "A") & (df["opponent"] == "C")) |
           ((df["you"] == "B") & (df["opponent"] == "A")) |
           ((df["you"] == "C") & (df["opponent"] == "B")))]

#indicies = np.concatenate([draws.index.values, loss.index.values])
#wins = df.drop(indicies)

draw_score = len(draws.index) * 3
win_score = len(wins.index) * 6

total_score = pick_score + draw_score + win_score

print()


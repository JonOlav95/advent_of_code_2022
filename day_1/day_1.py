import pandas as pd

# Keep the blank linkes and utilize them to group the elves
df = pd.read_csv("day_1_input.csv", skip_blank_lines=False, header=None, names=["calories"])

df["elf_number"] = df.isnull().all(axis=1).cumsum()
calories_sum = df.groupby("elf_number").sum()

highest_value = calories_sum["calories"].nlargest(1).values[0]
top_three = calories_sum["calories"].nlargest(3).sum()

print("Highest value: {}\nTop three: {}".format(highest_value, top_three))



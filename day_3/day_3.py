import pandas as pd


def calc_score(df):
    """Find all overlapping characters for each row in every column, then calculate the result.

    :param df: Dataframe containing elf rucksacks.
    :return: The sum of the priorties.
    """
    intersections = df.apply(lambda x: "".join(list(set.intersection(*map(set, list(x))))), axis=1)
    value = intersections.apply(lambda x: ord(x) - 96 if x.islower() else ord(x) - 38)

    print(value.sum())


def part_1(df):

    # Split each rucksack into two components
    df["compartment_1"] = df["rucksack"].apply(lambda x: x[:int(len(x) / 2)])
    df["compartment_2"] = df["rucksack"].apply(lambda x: x[int(len(x) / 2):])

    calc_score(df[["compartment_1", "compartment_2"]])


def part_2(df):

    # Split the rucksacks into three groups
    arr = df["rucksack"].values
    arr = arr.reshape(100, 3)
    df = pd.DataFrame(arr)

    calc_score(df)


def main():
    df = pd.read_csv("day_3_input.csv", header=None, names=["rucksack"])
    part_1(df)
    part_2(df)


if __name__ == "__main__":
    main()

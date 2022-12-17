import pandas as pd
import numpy as np
import re


def mark_signal(row, row_number, marks):

    distance = row["distance"]
    sensor_x = row["sensor_x"]
    sensor_y = row["sensor_y"]

    if sensor_y < row_number:
        distance_to_row = row_number - sensor_y

    elif sensor_y > row_number:
        distance_to_row = sensor_y - row_number
    else:
        distance_to_row = 0

    in_distance = distance - distance_to_row

    # Not in range of row
    if in_distance < 0:
        return

    # Start X, end X

    marks.append(set(range(sensor_x - in_distance, sensor_x + in_distance + 1)))


def main():
    df = pd.read_csv("day_15.txt", header=None, names=["sensor", "beacon"], sep=":")
    df["sensor"] = df["sensor"].apply(lambda x: list(map(int, re.findall(r"-?\d+", x))))
    df["beacon"] = df["beacon"].apply(lambda x: list(map(int, re.findall(r"-?\d+", x))))

    # df["sensor"] = df["sensor"].apply(lambda x: list(map(lambda z: z + 2, x)))
    # df["beacon"] = df["beacon"].apply(lambda x: list(map(lambda z: z + 2, x)))

    df["sensor_x"] = df["sensor"].apply(lambda x: x[0])
    df["sensor_y"] = df["sensor"].apply(lambda x: x[1])

    df["beacon_x"] = df["beacon"].apply(lambda x: x[0])
    df["beacon_y"] = df["beacon"].apply(lambda x: x[1])

    df["distance_x"] = df["sensor_x"] - df["beacon_x"]
    df["distance_y"] = df["sensor_y"] - df["beacon_y"]

    df["distance_x"] = df["distance_x"].apply(lambda x: abs(x))
    df["distance_y"] = df["distance_y"].apply(lambda x: abs(x))

    df["distance"] = df["distance_x"] + df["distance_y"]

    marks = []
    row_number = 2000000

    df.apply(mark_signal, row_number=row_number, marks=marks, axis=1)

    beacon_at_row = len(df[df["beacon_y"] == row_number]["beacon"].value_counts().index)
    sensor_at_row = len(df[df["sensor_y"] == row_number]["sensor"].value_counts().index)

    bound = set(range(0, 4000000))

    total_marks = sorted(set.union(*marks))
    total_marks = len(total_marks) - beacon_at_row - sensor_at_row
    print(total_marks)


if __name__ == "__main__":
    main()

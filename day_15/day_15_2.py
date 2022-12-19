import pandas as pd
import numpy as np
import re


def mark_signal(row, marks):
    distance = row["distance"]
    sensor_x = row["sensor_x"]
    sensor_y = row["sensor_y"]

    for row_number in range(400000):

        if sensor_y < row_number:
            distance_to_row = row_number - sensor_y

        elif sensor_y > row_number:
            distance_to_row = sensor_y - row_number
        else:
            distance_to_row = 0

        in_distance = distance - distance_to_row

        # Not in range of row
        if in_distance < 0:
            continue

        # Start X, end X

        x_start = sensor_x - in_distance
        x_end = sensor_x + in_distance + 1

        if x_start > 400000:
            continue

        if x_end < 0:
            continue

        if x_end > 400000:
            x_end = 400000

        if x_start < 0:
            x_start = 0

        marks.append(set(range(x_start, x_end)))


def extract(row, x_values, y_values):
    print()


def x_ranges(row):
    pass


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

    df["end_x1"] = df["sensor_x"] - df["distance"]
    df["end_x2"] = df["sensor_x"] + df["distance"]

    df["end_y1"] = df["sensor_y"] - df["distance"]
    df["end_y2"] = df["sensor_y"] + df["distance"]

    x_values = np.arange(0, 4000000, 1, dtype=int)
    y_values = np.arange(0, 4000000, 1, dtype=int)

    df.apply(x_ranges)
   # df.apply(extract, x_values=x_values, y_values=y_values, axis=1)



if __name__ == "__main__":
    main()

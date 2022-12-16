import pandas as pd
import numpy as np
import re


def place_tile(y, x, max_x, max_y):
    if y < 0:
        return
    elif x < 0:
        return
    elif y > max_y - 1:
        return
    elif x > max_x - 1:
        return



def mark_signal(row, max_x, max_y):

    distance = row["distance"]
    sensor_x = row["sensor_x"]
    sensor_y = row["sensor_y"]

    for x in range(sensor_x - distance, sensor_x):
        for i in range(sensor_x + x):
            place_tile(sensor_y + i, x, max_x, max_y)
            place_tile(sensor_y - i, x, max_x, max_y)

    for x in range(sensor_x + distance, sensor_x - 1, -1):
        for i in range(distance + sensor_x - x + 1):
            place_tile(sensor_y + i, x, max_x, max_y)
            place_tile(sensor_y - i, x, max_x, max_y)


def main():
    df = pd.read_csv("day_15.txt", header=None, names=["sensor", "beacon"], sep=":")
    df["sensor"] = df["sensor"].apply(lambda x: list(map(int, re.findall(r"-?\d+", x))))
    df["beacon"] = df["beacon"].apply(lambda x: list(map(int, re.findall(r"-?\d+", x))))

    # df["sensor"] = df["sensor"].apply(lambda x: list(map(lambda z: z + 2, x)))
    # df["beacon"] = df["beacon"].apply(lambda x: list(map(lambda z: z + 2, x)))

    df["sensor"] = df["sensor"].apply(lambda x: list([x[0] + 2, x[1]]))
    df["beacon"] = df["beacon"].apply(lambda x: list([x[0] + 2, x[1]]))

    df["sensor_x"] = df["sensor"].apply(lambda x: x[0])
    df["sensor_y"] = df["sensor"].apply(lambda x: x[1])

    df["beacon_x"] = df["beacon"].apply(lambda x: x[0])
    df["beacon_y"] = df["beacon"].apply(lambda x: x[1])

    max_size = df.max(axis=0)

    max_x = max_size[["sensor_x", "beacon_x"]].max(axis=0) + 1
    max_y = max_size[["sensor_y", "beacon_y"]].max(axis=0) + 1


    df["distance_x"] = df["sensor_x"] - df["beacon_x"]
    df["distance_y"] = df["sensor_y"] - df["beacon_y"]

    df["distance_x"] = df["distance_x"].apply(lambda x: abs(x))
    df["distance_y"] = df["distance_y"].apply(lambda x: abs(x))

    df["distance"] = df["distance_x"] + df["distance_y"]

    df.apply(mark_signal, max_x=max_x, max_y=max_y, axis=1)

    row = 10


    return


if __name__ == "__main__":
    main()

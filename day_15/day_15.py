import pandas as pd
import numpy as np
import re


def mark_signal(row, zone):
    # zone[row["sensor_y"], row["sensor_x"]] = 3
    # zone[row["sensor_y"], row["sensor_x"] + 1] = 3
    # zone[row["sensor_y"], row["sensor_x"] + 2] = 3
    # zone[row["sensor_y"], row["sensor_x"] + 3] = 3

    # zone[row["sensor_y"], row["sensor_x"] - 3] = 3
    # zone[row["sensor_y"] + 1, row["sensor_x"] - 2] = 3
    # zone[row["sensor_y"] - 1, row["sensor_x"] - 2] = 3

    # zone[row["sensor_y"], row["sensor_x"] - 1] = 3

    # zone[row["sensor_y"] + j, row["sensor_x"] + i + row["distance"]] = 3

    for x in range(row["distance"] + row["sensor_x"], row["sensor_x"], -1):
        for i in range(row["distance"] + row["sensor_x"] - x):
            pass

    for x in range(row["sensor_x"] - row["distance"], row["sensor_x"]):
        for i in range(row["sensor_x"] + x):
            zone[row["sensor_y"] + i, x] = 3
            zone[row["sensor_y"] - i, x] = 3



    print("")


def main():
    df = pd.read_csv("sample.txt", header=None, names=["sensor", "beacon"], sep=":")
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

    zone = np.zeros(shape=(max_y, max_x), dtype=int)

    df["distance_x"] = df["sensor_x"] - df["beacon_x"]
    df["distance_y"] = df["sensor_y"] - df["beacon_y"]

    df["distance_x"] = df["distance_x"].apply(lambda x: abs(x))
    df["distance_y"] = df["distance_y"].apply(lambda x: abs(x))

    df["distance"] = df["distance_x"] + df["distance_y"]

    zone[df["sensor_y"], df["sensor_x"]] = 1
    zone[df["beacon_y"], df["beacon_x"]] = 2

    df.apply(mark_signal, zone=zone, axis=1)

    return


if __name__ == "__main__":
    main()

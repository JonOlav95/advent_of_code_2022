import pandas as pd
import numpy as np
import re


def pour_sand(cave, p2):
    sand_x = pour = 37
    sand_y = 0
    sand_count = 0

    while True:

        if sand_y + 2 > len(cave):
            break

        if sand_x + 2 > len(cave[0]):
            if not p2:
                break

            new_floor = np.zeros(shape=(len(cave), 1), dtype=int)
            new_floor[-1] = 1
            cave = np.hstack([cave, new_floor])

        if sand_x <= 0:
            if not p2:
                break

            new_floor = np.zeros(shape=(len(cave), 1), dtype=int)
            new_floor[-1] = 1
            pour += 1
            cave = np.hstack([new_floor, cave])

        if cave[sand_y + 1, sand_x] == 0:
            sand_y += 1
            continue

        if cave[sand_y + 1, sand_x - 1] == 0:
            sand_y += 1
            sand_x -= 1
            continue

        if cave[sand_y + 1, sand_x + 1] == 0:
            sand_y += 1
            sand_x += 1
            continue

        if sand_y == 0:
            break
        sand_count += 1

        cave[sand_y, sand_x] = 2
        sand_x = pour
        sand_y = 0

    print(sand_count)


def f(row):
    row = row[0]
    y_values = re.findall(r",(\d+)", row)
    x_values = re.findall(r"(\d+),", row)

    y_values = np.array(list(map(int, y_values)))
    x_values = np.array(list(map(int, x_values)))
    return y_values, x_values


def main():
    values = pd.read_csv("day_14.txt", header=None, sep="\r\n", engine="python").values

    arr = np.array(list(map(f, values)), dtype=object)

    max_y = max(list(map(np.amax, arr[:, 0]))) + 1

    max_x = max(list(map(np.amax, arr[:, 1]))) + 1
    min_x = min(list(map(np.amin, arr[:, 1])))
    pour = 500

    max_x -= min_x
    arr[:, 1] -= min_x
    pour -= min_x

    cave = np.zeros(shape=(max_y, max_x), dtype=int)

    for row in arr:
        y = row[0]
        x = row[1]

        for i in range(len(row[0]) - 1):

            y_s = y[i]
            y_e = y[i + 1]

            x_s = x[i]
            x_e = x[i + 1]

            distance_y = y_s - y_e
            if distance_y > 0:
                y_s, y_e = y_e, y_s

            distance_x = x_s - x_e
            if distance_x > 0:
                x_s, x_e = x_e, x_s

            cave[y_s:y_e + 1, x_s:x_e + 1] = 1

    pour_sand(cave, p2=False)

    cave = np.where(cave == 1, cave, 0)
    cave = np.vstack([cave, np.zeros(shape=(2, max_x), dtype=int)])
    cave[-1, :] = 1

    pour_sand(cave, p2=True)


if __name__ == "__main__":
    main()

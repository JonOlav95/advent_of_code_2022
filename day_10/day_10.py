import pandas as pd
import re


def checkem(cyc, val):
    tmp = val * cyc
    if cyc == 20:
        return val * cyc
    if cyc == 60:
        return val * cyc
    if cyc == 100:
        return val * cyc
    if cyc == 140:
        return val * cyc
    if cyc == 180:
        return val * cyc
    if cyc == 220:
        return val * cyc

    return 0


arr = pd.read_csv("day_10.txt", header=None).values.squeeze()

x = 1
cycle = 1
zum = 0

for i in range(len(arr)):

    if "noop" in arr[i]:
        cycle += 1
        zum += checkem(cycle, x)

    if "addx" in arr[i]:
        value = re.findall(r"-?\d+", arr[i])[0]
        cycle += 1

        zum += checkem(cycle, x)
        cycle += 1

        x += int(value)
        zum += checkem(cycle, x)

print(zum)

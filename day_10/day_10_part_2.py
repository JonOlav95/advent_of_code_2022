import pandas as pd
import re
import numpy as np


def draw(spir, cyc):
    if "#" in spir[cyc]:
        return "#"
    else:
        return "."


arr = pd.read_csv("day_10.txt", header=None).values.squeeze()

x = 1
cycle = 0
zum = 0

spirit = np.array(list("###....................................."))
drawing = []
drawing_list = []

for i in range(len(arr)):

    if "noop" in arr[i]:
        drawing.append(draw(spirit, cycle))
        cycle += 1

        if cycle == 40:
            spirit = np.array(list("###....................................."))
            drawing_list.append(drawing)
            drawing = []
            cycle = 0

    if "addx" in arr[i]:
        value = re.findall(r"-?\d+", arr[i])[0]
        drawing.append(draw(spirit, cycle))

        cycle += 1

        if cycle == 40:
            length = len(drawing)
            spirit = np.array(list("###....................................."))
            drawing_list.append(drawing)
            drawing = []
            cycle = 0

        drawing.append(draw(spirit, cycle))
        x += int(value)
        spirit[:] = "."
        spirit[x - 1: x + 2] = "###"

        cycle += 1

        if cycle == 40:
            length = len(drawing)
            spirit = np.array(list("###....................................."))
            drawing_list.append(drawing)
            drawing = []
            cycle = 0


result = np.array(drawing_list)


for a in range(len(drawing_list)):
    for b in range(len(drawing_list[a])):
        if drawing_list[a][b] == ".":
            drawing_list[a][b] = " "

df = pd.DataFrame(drawing_list)

abc = np.char.replace(result, ".", " ")
abc = abc.reshape(-1, 1)
abc = np.expand_dims(abc, axis=2)
df = pd.DataFrame(abc)
for i in range(len(abc)):
    print(abc[i])

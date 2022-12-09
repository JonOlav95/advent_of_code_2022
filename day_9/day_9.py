import pandas as pd
import re
import numpy as np

matrix = [[0 for x in range(2)] for y in range(10)]

p1_sol = []
p2_sol = []

with open("day_9.txt") as file:
    for line in file:

        direction = line[0]
        amount = int(re.findall(r"\d+", line)[0])

        for i in range(amount):
            head = matrix[0]

            if direction == "D":
                head[1] -= 1

            elif direction == "U":
                head[1] += 1

            elif direction == "L":
                head[0] -= 1

            elif direction == "R":
                head[0] += 1

            for j in range(1, len(matrix)):
                prev = matrix[j - 1]
                current = matrix[j]

                x_neighbour = (current[0] - 1) <= prev[0] <= (current[0] + 1)
                y_neighbour = (current[1] - 1) <= prev[1] <= (current[1] + 1)

                if current[0] < prev[0]:
                    x_vel = 1
                else:
                    x_vel = -1

                if current[1] < prev[1]:
                    y_vel = 1
                else:
                    y_vel = -1

                if not x_neighbour and not (current[1] == prev[1]):
                    current[0] += x_vel
                    current[1] += y_vel

                elif not x_neighbour:
                    current[0] += x_vel

                elif not y_neighbour and not (current[0] == prev[0]):
                    current[0] += x_vel
                    current[1] += y_vel

                elif not y_neighbour:
                    current[1] += y_vel

            p1_sol.append([matrix[1][0], matrix[1][1]])
            p2_sol.append([matrix[-1][0], matrix[-1][1]])

p1 = np.unique(p1_sol, axis=0)
p2 = np.unique(p2_sol, axis=0)

print(len(p1))
print(len(p2))

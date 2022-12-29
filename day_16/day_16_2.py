from copy import copy
from itertools import compress

import pandas as pd
import re
import numpy as np


class Node:
    def __init__(self, idx, fr):
        self.idx = idx
        self.fr = fr
        self.visited = False
        self.open = False
        self.neighbours = []

    def add_neighbour(self, neighbour, dist):
        self.neighbours.append([neighbour, dist])

    def __eq__(self, other):
        if self.idx == other:
            return True
        return False


def create_neighbours(row, graph):
    node = [x for x in graph if x.idx == row["valve"]][0]

    for lead in row["leads_to"]:
        lead = [x for x in graph if x.idx == lead][0]
        node.add_neighbour(lead, 1)


def create_node(row):
    node = Node(row["valve"], int(row["flow_rate"]))
    return node


def recursion(node, add_node, distance):
    if node == add_node:
        return

    for n in node.neighbours:
        if n[0] == add_node:
            if distance <= n[1]:
                node.neighbours.remove(n)

            if distance > n[1]:
                return

            break

    node.add_neighbour(add_node, distance)

    for neigh in add_node.neighbours:
        if neigh[1] > 1:
            continue

        recursion(node, neigh[0], distance + neigh[1])


def sort_by_max(start_node, minute):
    length = len(start_node.neighbours) - 1
    values = []

    for neigh in start_node.neighbours:
        neighbour = neigh[0]
        distance = neigh[1]

        value = neighbour.fr * (minute - distance - 1)
        values.append(value)

    for i in range(length):
        for j in range(0, length - i):
            if values[j] < values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                start_node.neighbours[j], start_node.neighbours[j + 1] = start_node.neighbours[j + 1], \
                    start_node.neighbours[j]

    return values


def move_func(node, minute, flow):
    for ndistance in node.neighbours:
        neighbour = ndistance[0]

        if neighbour.visited:
            continue

        m = minute - ndistance[1] - 1

        if m <= 0:
            continue

        neighbour.visited = True
        f = m * neighbour.fr

        return f + flow, m, neighbour

    return flow, 0, node


def part_2(start_node):
    m1 = m2 = 26
    f1 = f2 = 0
    n1 = n2 = start_node

    while True:

        if m1 >= m2:
            f1, m1, n1 = move_func(n1, m1, f1)
        else:
            f2, m2, n2 = move_func(n2, m2, f2)

        if m1 == m1 == 0:
            m1 = m2 = 26
            f1 = f2 = 0
            n1 = n2 = start_node


def part_2_2(n1, n2, m1, m2, f1, f2, max1, max2):
    fr_1 = sort_by_max(n1, m1)
    fr_2 = sort_by_max(n2, m2)

    if m1 >= m2:

        for i in range(len(fr_1)):
            neighbour = n1.neighbours[i][0]
            distance = n1.neighbours[i][1]

            if neighbour.open:
                continue

            if m1 - distance - 1 <= 0:
                continue

            m = m1 - distance - 1
            neighbour.open = True
            max1, max2 = part_2_2(neighbour, n2, m, m2, f1 + fr_1[i], f2, max1, max2)
            neighbour.open = False

    else:

        for i in range(len(fr_2)):

            neighbour = n2.neighbours[i][0]
            distance = n2.neighbours[i][1]

            if neighbour.open:
                continue

            if m2 - distance - 1 <= 0:
                continue

            m = m2 - distance - 1
            neighbour.open = True
            max1, max2 = part_2_2(n1, neighbour, m1, m, f1, f2 + fr_2[i], max1, max2)
            neighbour.open = False

    if (f1 + f2) > (max1 + max2):
        return f1, f2

    return max1, max2


def main():
    df = pd.read_csv("day_16.txt", header=None, names=["full_text"], sep=".")

    df["flow_rate"] = df["full_text"].apply(lambda x: re.search(r"-?\d+", x).group())

    df["valve"] = df["full_text"].apply(lambda x: re.findall(r"\b[A-Z]{2}\b", x)[0])
    df["leads_to"] = df["full_text"].apply(lambda x: re.findall(r"\b[A-Z]{2}\b", x)[1:])

    graph = df.apply(create_node, axis=1).values
    df.apply(create_neighbours, graph=graph, axis=1)

    for i in range(len(graph)):
        node = graph[i]

        neighbours = copy(node.neighbours)
        node.visited = True

        for neig in neighbours:
            recursion(node, neig[0], 1)

        for n in graph:
            n.visited = False

    start_node = [n for n in graph if n.idx == "AA"][0]

    for node in graph:
        node.neighbours = [n for n in node.neighbours if n[0].fr != 0]

    # graph = [subl for subl in graph if subl.fr != 0]
    f1, f2 = part_2_2(start_node, start_node, 26, 26, 0, 0, 0, 0)
    print(f1 + f2)


if __name__ == "__main__":
    main()

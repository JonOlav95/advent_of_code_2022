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


def part_1(node, minute, flow_rate, max_flow):


    fr = sort_by_max(node, minute)

    for i in range(len(fr)):
        neighbour = node.neighbours[i][0]
        distance = node.neighbours[i][1]

        if neighbour.open:
            continue

        if minute - distance <= 0:
            continue

        neighbour.open = True

        max_flow = part_1(neighbour, minute - distance - 1, flow_rate + fr[i], max_flow)

    print(flow_rate)
    node.open = False

    if flow_rate > max_flow:
        return flow_rate

    return max_flow


def main():
    df = pd.read_csv("sample.txt", header=None, names=["full_text"], sep="<>")

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

    #graph = [subl for subl in graph if subl.fr != 0]

    max_flow = part_1(start_node, 30, 0, 0)

    print(max_flow)


if __name__ == "__main__":
    main()

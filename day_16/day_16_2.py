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


def from_to(graph, from_node, to_node):
    visited_nodes = [from_node]


def rec(graph, cnode, acc_flow, minute):
    for key, neighbours in graph.node_dict.items():
        print("")
    print("x")


def create_node(row):
    node = Node(row["valve"], int(row["flow_rate"]))
    return node


def move_neighbours(from_node, to_node):
    if from_node == to_node:
        return

    neighbours = [subl for subl in to_node.neighbours if from_node not in subl]

    if neighbours == to_node.neighbours:
        return

    from_neighbours = from_node.neighbours

    for new_neigh in from_neighbours:
        if new_neigh not in to_node.neighbours:
            to_node.add_neighbour(new_neigh[0], new_neigh[1] + 1)

    if to_node.fr == 0:
        for neigh in to_node.neighbours:
            move_neighbours(to_node, neigh[0])


def main():
    df = pd.read_csv("sample.txt", header=None, names=["full_text"], sep="<>")

    df["flow_rate"] = df["full_text"].apply(lambda x: re.search(r"-?\d+", x).group())

    df["valve"] = df["full_text"].apply(lambda x: re.findall(r"\b[A-Z]{2}\b", x)[0])
    df["leads_to"] = df["full_text"].apply(lambda x: re.findall(r"\b[A-Z]{2}\b", x)[1:])

    graph = df.apply(create_node, axis=1).values
    df.apply(create_neighbours, graph=graph, axis=1)


    for node in graph:
        if node.fr != 0:
            continue

        for n in graph:
            move_neighbours(node, n)

    graph = [subl for subl in graph if subl.fr != 0]


if __name__ == "__main__":
    main()

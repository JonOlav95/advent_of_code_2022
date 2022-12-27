from itertools import compress

import pandas as pd
import re
import numpy as np


class Graph:

    def __init__(self):
        self.node_dict = {}

    def add_node(self, idx):
        self.node_dict[idx] = []

    def add_edge(self, frm, to, weight):
        self.node_dict[frm].append([to, weight])


class Node:
    def __init__(self, idx, fr, neigh):
        self.idx = idx
        self.fr = fr
        self.neigh = neigh


def func(row, graph):

    for node in row["leads_to"]:
        graph.add_edge(row["valve"], node, 1)


def main():

    df = pd.read_csv("sample.txt", header=None, names=["full_text"], sep="<>")

    df["flow_rate"] = df["full_text"].apply(lambda x: re.search(r"-?\d+", x).group())

    df["valve"] = df["full_text"].apply(lambda x: re.findall(r"\b[A-Z]{2}\b", x)[0])
    df["leads_to"] = df["full_text"].apply(lambda x: re.findall(r"\b[A-Z]{2}\b", x)[1:])

    graph = Graph()
    df["valve"].apply(lambda x: graph.add_node(x))
    df.apply(func, graph=graph, axis=1)

    zero_fr = df[df["flow_rate"] == "0"]["valve"]
    zero_fr = zero_fr[zero_fr != "AA"].values

    for v in zero_fr:
        t_nodes = graph.node_dict[v]
        graph.node_dict.pop(v)

        t_nodes = np.array(t_nodes)
        t_nodes[:, 1] = t_nodes[:, 1].astype(int) + 1
        t_nodes = t_nodes.tolist()

        for key, neighbours in graph.node_dict.items():

            if key == v:
                continue

            neigh = list(compress(neighbours, [v in subl for subl in neighbours]))

            if not neigh:
                continue

            neighbours = [subl for subl in neighbours if v not in subl]

            for t in t_nodes:
                if t[0] != key:
                    neighbours.append(t)

            graph.node_dict[key] = neighbours

    

    return


if __name__ == "__main__":
    main()
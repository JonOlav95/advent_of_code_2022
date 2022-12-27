import pandas as pd
import numpy as np
import re


def rec(graph, current_node, minutes, accum_flow):

    if minutes <= 0:
        print(accum_flow)

        return

    minutes -= 1
    accum_flow += current_node.flow_rate * minutes


    for node in graph:
        pass


class Node:
    def __init__(self, name, flow_rate, leads_to):
        self.name = name
        self.flow_rate = flow_rate
        self.leads_to = leads_to
        self.visited = False
        self.opened = False

        self.distance = 0


def create_graph(row):
    node = Node(row["valve"], int(row["flow_rate"]), row["leads_to"])

    return node


def part_1(graph):
    minutes = 30
    lambda_func = np.vectorize(lambda x: x.name == "AA")
    current_node = graph[lambda_func(graph)][0]
    visited_nodes = [current_node]
    acc_flow = 0

    while minutes > 0:
        for node in graph:
            node.visited = False
            node.distance = 0

        max_flow = -9999
        max_node = None

        while visited_nodes:
            current_node = visited_nodes.pop(0)

            for node in current_node.leads_to:
                debug_name = node
                lambda_func = np.vectorize(lambda x: x.name == node)
                node = graph[lambda_func(graph)][0]

                if node.visited or node.opened:
                    continue

                node.distance = current_node.distance + 1
                time_left = minutes - node.distance

                # Time to open
                time_left -= 1

                total_flow = time_left * node.flow_rate

                if total_flow > max_flow:
                    max_flow = total_flow
                    max_node = node

                node.visited = True
                visited_nodes.append(node)

        if max_node:
            acc_flow += max_flow
            minutes = time_left
            max_node.opened = True
            visited_nodes = [max_node]
            print(max_node.name)
        else:
            break

    print(acc_flow)


def main():
    df = pd.read_csv("sample.txt", header=None, names=["full_text"], sep="<>")
    df["flow_rate"] = df["full_text"].apply(lambda x: re.search(r"-?\d+", x).group())

    df["valve"] = df["full_text"].apply(lambda x: re.findall(r"\b[A-Z]{2}\b", x)[0])
    df["leads_to"] = df["full_text"].apply(lambda x: re.findall(r"\b[A-Z]{2}\b", x)[1:])

    graph = df.apply(create_graph, axis=1).values

    part_1(graph)

    return


if __name__ == "__main__":
    main()

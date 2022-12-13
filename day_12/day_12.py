import collections

import pandas as pd
import numpy as np
import sys

step_solution = 9999

sys.setrecursionlimit(10000)


class Node:

    def __init__(self, y, x, value):
        self.y = y
        self.x = x
        self.value = value
        self.nodes = []
        self.visited = False


def bfs(grid, start, end_y, end_x, max_x, max_y):
    queue = collections.deque([[start]])
    seen = {start}

    while queue:
        path = queue.popleft()
        x, y = path[0].x, path[0].y

        if y == end_y and x == end_x:
            return path

        positions = [(y, x + 1), (y, x - 1), (y - 1, x), (y + 1, x)]

        for pos in positions:
            if sum(n < 0 for n in pos) > 0:
                continue

            if pos[0] >= max_y or pos[1] >= max_x:
                continue

            queue.append(path + [pos])
            seen.add(pos)


def main():
    def build_nodes():

        node_arr = np.empty((len(arr), len(arr[0])), dtype=object)

        for x in range(max_x):
            for y in range(max_y):
                value = ord(arr[y, x])
                node = Node(y, x, value)
                node_arr[y, x] = node

        return node_arr

    def build_connection(node_arr):

        for x in range(max_x):
            for y in range(max_y):
                current_node = node_arr[y, x]
                value = current_node.value

                positions = [(y, x + 1), (y, x - 1), (y - 1, x), (y + 1, x)]

                for pos in positions:

                    if sum(n < 0 for n in pos) > 0:
                        continue

                    if pos[0] >= max_y or pos[1] >= max_x:
                        continue

                    travel_value = node_arr[pos].value

                    if value >= travel_value - 1:
                        current_node.nodes.append(node_arr[pos])

        return node_arr

    arr = pd.read_csv("day_12.txt", header=None).values.squeeze()
    arr = np.array(list((map(list, arr))))

    start = np.where(arr == "S")
    end = np.where(arr == "E")

    start_y = start[0][0]
    start_x = start[1][0]

    end_y = end[0][0]
    end_x = end[1][0]

    arr[start_y, start_x] = "a"
    arr[end_y, end_x] = "z"

    max_y = len(arr)
    max_x = len(arr[0])

    travel_history = np.full((len(arr), len(arr[0])), 0)

    graph = build_nodes()
    graph = build_connection(graph)
    bfs(graph, graph[start_y, start_x], end_y, end_x, max_x, max_y)

    print()


if __name__ == "__main__":
    main()

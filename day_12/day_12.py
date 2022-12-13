import collections
from copy import copy

import pandas as pd
import numpy as np
import sys
from queue import PriorityQueue
import heapq


class Node:

    def __init__(self):
        self.value = -1
        self.distance = 999999
        self.position = 0
        self.visited = False
        

def find_smallest(graph):
    distance = 9999999
    min_node = None
    for y in range(len(graph)):
        for x in range(len(graph[0])):

            if graph[y, x].visited:
                continue

            if graph[y, x].distance < distance:
                distance = graph[y, x].distance
                min_node = graph[y, x]

    return min_node


def dijkstra(arr, start, end):

    graph = np.empty((len(arr), len(arr[0])), dtype=object)
    unvisited = []

    for y in range(len(arr)):
        for x in range(len(arr[0])):
            node = Node()
            node.position = (y, x)
            node.value = arr[y, x]
            graph[y, x] = node
            unvisited.append(node)

    graph[start].distance = 0
    travel_chart = np.zeros((len(arr), len(arr[0])), dtype=int)
    while True:

        current_node = find_smallest(graph)

        if current_node.distance > 100000:
            return 100000

        current_node.visited = True
        y, x = current_node.position
        travel_chart[y, x] = 1

        if (y, x) == end:
            print(current_node.distance)
            return current_node.distance

        positions = [(y, x + 1), (y, x - 1), (y - 1, x), (y + 1, x)]

        for pos in positions:

            if sum(n < 0 for n in pos) > 0:
                continue

            if pos[0] >= len(arr) or pos[1] >= len(arr[0]):
                continue

            if current_node.value < graph[pos].value - 1:
                continue

            travel_node = graph[pos]
            distance = current_node.distance + 1

            if travel_node.distance > distance:
                travel_node.distance = distance


def main():
    arr = pd.read_csv("day_12.txt", header=None).values.squeeze()
    arr = np.array(list((map(list, arr))))

    start = np.where(arr == "S")
    end = np.where(arr == "E")

    start = (start[0][0], start[1][0])
    end = (end[0][0], end[1][0])

    arr[start] = "a"
    arr[end] = "z"

    maze = arr.view(np.int32) - 96


    # BRUTE FORCE WINS
    ways = []
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y, x] == "a":
                value = dijkstra(copy(maze), (y, x), end)
                ways.append(value)

    ways.sort()
    print(ways)


if __name__ == "__main__":
    main()

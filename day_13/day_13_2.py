import pandas as pd
import numpy as np
import ast


def rec(list_1, list_2):
    if isinstance(list_1, int) and isinstance(list_2, list):
        list_1 = [list_1]

    if isinstance(list_2, int) and isinstance(list_1, list):
        list_2 = [list_2]

    if isinstance(list_2, int) and isinstance(list_1, int):
        if list_1 < list_2:
            return True
        elif list_2 < list_1:
            return False
        else:
            return None

    if not list_1 and not list_2:
        return None
    elif not list_1:
        return True
    elif not list_2:
        return False

    if isinstance(list_1[0], list) or isinstance(list_2[0], list):

        for i in range(len(list_1)):
            if i > len(list_2) - 1:
                return False

            right_order = rec(list_1[i], list_2[i])
            if right_order is None:
                continue

            return right_order

        return True

    for i in range(len(list_1)):
        if i > len(list_2) - 1:
            return False

        if isinstance(list_1[i], list) or isinstance(list_2[i], list):
            return rec(list_1[i], list_2[i])

        if list_1[i] > list_2[i]:
            return False

        if list_1[i] < list_2[i]:
            return True

    if len(list_2) > len(list_1):
        return True

    return None


def main():
    with open("day_13.txt") as file:
        lines = file.read().split("\n")

    lines = [e for e in lines if e != ""]
    lines = [ast.literal_eval(e) for e in lines]
    lines.append([[2]])
    lines.append([[6]])

    count = 0
    for i in range(len(lines) - 1):
        for j in range(len(lines) - i - 1):
            count += 1
            print(count)
            if count == 105:
                print("s")

            # Line J  NOT smaller than line j + 1
            if not rec(lines[j], lines[j + 1]):
                lines[j], lines[j + 1] = lines[j + 1], lines[j]

    print("x")


if __name__ == "__main__":
    main()

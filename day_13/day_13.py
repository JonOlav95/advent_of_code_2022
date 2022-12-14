import pandas as pd
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

        if list_1[i] > list_2[i]:
            return False

        if list_1[i] < list_2[i]:
            return True

    if len(list_2) > len(list_1):
        return True

    return None


def main():
    with open("day_13.txt") as file:
        lines = file.read().split("\n\n")

    counter = 0
    right_order = 0
    for line in lines:
        counter += 1
        line_1, line_2 = line.split("\n")
        list_1 = ast.literal_eval(line_1)
        list_2 = ast.literal_eval(line_2)

        if rec(list_1, list_2):
            right_order += counter

    print(right_order)


if __name__ == "__main__":
    main()

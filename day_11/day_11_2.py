import math

import pandas as pd
import re


class Monkey:

    def __init__(self, number, items, operation, test, true, false):
        self.number = number
        self.items = items

        self.operation = operation
        self.test_value = test
        self.true_throw = true
        self.false_throw = false
        self.inspection = 0

    def play(self, monkeys):
        values = []
        to = []

        for item in self.items:
            self.inspection += 1

            value = self.operation(item)

            if value % self.test_value == 0:

                new_value = 1

                for m in monkeys:
                    tmp = value
                    tmp = m.operation(tmp)

                    if tmp % m.test_value:
                        new_value *= tmp

                value = new_value
                to.append(self.true_throw)

            else:
                to.append(self.false_throw)

            values.append(value)

        self.items = []
        return values, to


def create_monkey(lines):
    number = int(re.findall(r"\d+", lines[0])[0])
    items = re.findall(r"\d+", lines[1])
    items = list(map(int, items))

    operation = re.findall(r"old.*", lines[2])[0]

    ##operation_value = re.findall(r"-?\d+", lines[2])[0]
    # operation_type = re.findall(r"[+*]", lines[2])[0]

    operation = "lambda old: " + operation
    operation = eval(operation)

    test = int(re.findall(r"-?\d+", lines[3])[0])
    true = int(re.findall(r"\d+", lines[4])[0])
    false = int(re.findall(r"\d+", lines[5])[0])

    monkey = Monkey(number, items, operation, test, true, false)

    return monkey


def main():
    with open("sample.txt") as file:
        lines = file.readlines()
        monkeys = []

        for i in range(0, len(lines), 7):
            monkeys.append(create_monkey(lines[i:i + 7]))

    test_values = []
    for monkey in monkeys:
        test_values.append(monkey.test_value)

    rounds = 20
    for i in range(rounds):
        print(i)
        for monkey in monkeys:
            values, to = monkey.play(monkeys)

            for j in range(len(to)):
                monkeys[to[j]].items.append(values[j])

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspection)

    inspections.sort(reverse=True)
    solution = inspections[0] * inspections[1]
    print(solution)


if __name__ == "__main__":
    main()

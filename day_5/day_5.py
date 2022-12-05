import pandas as pd
import numpy as np
import re


def func(stacks, commands, reverse=True):
    for i in range(len(commands)):

        digits = re.findall(r"\d+", commands[i])
        amount = int(digits[0])
        from_supply = int(digits[1]) - 1
        to_supply = int(digits[2]) - 1

        stacks[from_supply], removed = stacks[from_supply][:-amount], stacks[from_supply][-amount:]

        if reverse:
            removed = removed[::-1]

        stacks[to_supply] += removed

    tmp = np.array([x[-1] for x in stacks])
    tmp = "".join(tmp)
    print(tmp)


def main():
    # YIKES
    df = pd.read_csv("day_5_cpy.txt", names=["string"], header=None)
    commands = df[9:]
    supply = df[:8]

    supply = supply.replace("    ", "[0]", regex=True)
    supply = supply.replace(r" |\[|\]", "", regex=True)
    supply = supply["string"].apply(lambda z: pd.Series(list(z)))
    stacks = supply.transpose().sum(axis=1)
    stacks = stacks.apply(lambda z: z[::-1])
    stacks = stacks.replace("0", "", regex=True)
    stacks = stacks.values
    commands = np.squeeze(commands.values)

    func(stacks.copy(), commands, reverse=True)
    func(stacks, commands, reverse=False)


if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np

step_solution = 9999


def main():
    def function(y, x, steps=0):
        global step_solution
        if step_solution < steps:
            return

        if travel_history[y, x] == 4:
            return

        x_distance = x - end_x
        y_distance = y - end_y

        if x_distance > 0:
            move_left = abs(x_distance)
            move_right = -abs(x_distance)
        else:
            move_left = -abs(x_distance)
            move_right = abs(x_distance)

        if y_distance > 0:
            move_up = abs(y_distance)
            move_down = -abs(y_distance)
        else:
            move_up = -abs(y_distance)
            move_down = abs(y_distance)

        # R L U P
        positions = [(y, x + 1), (y, x - 1), (y - 1, x), (y + 1, x)]
        tmp_arr = [move_right, move_left, move_up, move_down]
        positions = [x for _, x in sorted(zip(tmp_arr, positions), reverse=True)]

        letter = arr[y, x]

        if x == end_x and y == end_y:
            
            if steps < step_solution:
                step_solution = steps
            
            print(steps)
            win_length.append(steps)
            return

        travel_history[y, x] += 1

        for pos in positions:

            if sum(n < 0 for n in pos) > 0:
                continue

            if pos[0] > max_y or pos[1] > max_x:
                continue

            travel_letter = arr[pos]

            if travel_history[pos] >= 1:
                continue

            if ord(letter) >= ord(travel_letter) - 1:
                function(*pos, steps + 1)

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

    win_length = []
    step_limit = 999999999

    max_y = len(arr) - 1
    max_x = len(arr[0]) - 1

    travel_history = np.full((len(arr), len(arr[0])), 0)

    function(start_y, start_x)
    win_length.sort()
    print(win_length)


if __name__ == "__main__":
    main()

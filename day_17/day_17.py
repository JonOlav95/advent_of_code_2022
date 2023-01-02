import numpy as np
import pandas as pd


def move_left(board, shape):
    p1_slice = board[shape]

    if 1 in p1_slice:
        return False

    return True


def move_right(board, shape):
    p1_slice = board[shape]

    if 1 in p1_slice:
        return False

    return True


def move_down(board, shape):
    p1_slice = board[shape]

    if 1 in p1_slice:
        return False

    return True


def get_shapes(s_index, y, x):
    shapes = [np.s_[y, x:x + 4],
              np.s_[(y, y + 1, y + 1, y + 1, y + 2), (x + 1, x, x + 1, x + 2, x + 1)],
              np.s_[(y, y + 1, y + 2, y + 2, y + 2), (x + 2, x + 2, x, x + 1, x + 2)],
              np.s_[y:y + 4, x],
              np.s_[y:y + 2, x:x + 2]]

    return shapes[s_index]


def main():
    move = pd.read_csv("sample.txt", header=None)[0].values[0]

    board = [[1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1]]

    board = np.array(board)

    x = 3
    y = 0
    m_index = 0
    s_index = 0
    rock_count = 0

    while True:

        if move[m_index] == ">":
            shape = get_shapes(s_index, y, x + 1)
            if move_right(board, shape):
                x += 1

        elif move[m_index] == "<":
            shape = get_shapes(s_index, y, x - 1)
            if move_left(board, shape):
                x -= 1

        shape = get_shapes(s_index, y + 1, x)
        if move_down(board, shape):
            y += 1
            board[shape] = 2
            board[shape] = 0
        else:
            shape = get_shapes(s_index, y, x)
            board[shape] = 1
            s_index += 1

            if s_index == 5:
                s_index = 0

            a = -1
            if s_index == 0:
                a = 1
            elif s_index == 1:
                a = 3
            elif s_index == 2:
                a = 3
            elif s_index == 3:
                a = 4
            elif s_index == 4:
                a = 2

            for i in range(y, 3 + a):
                board = np.concatenate((np.array([[1, 0, 0, 0, 0, 0, 0, 0, 1]]), board))

            if y > 3 + a:
                y = y - 3 - a
            else:
                y = 0

            rock_count += 1
            x = 3

        m_index += 1

        if m_index == len(move):
            m_index = 0

        if rock_count == 2022:
            break

    print(len(board) - 3)


if __name__ == "__main__":
    main()

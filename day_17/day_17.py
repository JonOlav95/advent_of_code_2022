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


def sizes(idx):
    if idx == 0:
        return 1
    elif idx == 1:
        return 3
    elif idx == 2:
        return 3
    elif idx == 3:
        return 4
    elif idx == 4:
        return 2

    print("abcdvsdcvds")
    return -1


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

    # ROCK COUNT 31
    while True:

        if rock_count == 30:
            print()
        shape = get_shapes(s_index, y, x)
        board[shape] = 2
        board[shape] = 0
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
        else:
            shape = get_shapes(s_index, y, x)
            board[shape] = 1
            s_index += 1

            if s_index == 5:
                s_index = 0

            a = sizes(s_index)
            height = 0

            for i in range(len(board)):
                tmp = board[i, 1:-1]
                if 1 in tmp:
                    break
                else:
                    height += 1

            if height > 3 + a:
                y = height - 3 - a
            else:
                for i in range(height, 3 + a):
                    board = np.concatenate((np.array([[1, 0, 0, 0, 0, 0, 0, 0, 1]]), board))

                y = 0

            rock_count += 1
            x = 3

            if 0 not in board[height, :]:
                print()

        m_index += 1

        if m_index == len(move):
            m_index = 0

        if m_index == 0 and s_index == 0:
            print()

        if rock_count > 615 and m_index == 0:
            break

    height = 0
    print(rock_count)

    for i in range(len(board)):
        tmp = board[i, 1:-1]
        if 1 in tmp:
            break
        else:
            height += 1

    print(len(board) - height - 1)


if __name__ == "__main__":
    main()

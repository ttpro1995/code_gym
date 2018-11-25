__author__ = "Thai Thien"
__link__ = "https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn"

import numpy as np


def find_dub(a):
    """
    find dublicate number in numpy array
    :param a:
    :return:
    """
    a = a[a!='.'].astype(int)
    u, i = np.unique(a, return_inverse=True)
    u2 = np.unique(a)
    x = u[np.bincount(i) > 1]
    return x


def sudoku2(grid):
    """
    check if it is sudoku
    :param grid:
    :return:
    """
    # print(npgrid[0])
    # x = find_dub(npgrid[0])
    # y = x[x!='.']
    # print(y)
    # print(len(y))
    npgrid = np.array(grid)
    sub_grid = []
    sub_grid.append(npgrid[0:3, 0:3])
    sub_grid.append(npgrid[3:6, 0:3])
    sub_grid.append(npgrid[6:9, 0:3])
    sub_grid.append(npgrid[0:3, 3:6])
    sub_grid.append(npgrid[3:6, 3:6])
    sub_grid.append(npgrid[6:9, 3:6])
    sub_grid.append(npgrid[0:3, 6:9])
    sub_grid.append(npgrid[3:6, 6:9])
    sub_grid.append(npgrid[6:9, 6:9])

    print(sub_grid)

    # row
    for i in range(9):
        print(npgrid[i])
        if len(find_dub(npgrid[i])) > 0:
            print("FALSE")
            return False

    # column
    for i in range(9):
        print(npgrid[:, i])
        if len(find_dub(npgrid[:, i])) > 0:
            print("FALSE")
            return False

    # subgrid
    for i in sub_grid:
        print(i)
        if len(find_dub(i)) > 0:
            print("FALSE")
            return False
    return True
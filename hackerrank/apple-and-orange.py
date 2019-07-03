#!/bin/python3

__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"
__url__ = "https://www.hackerrank.com/challenges/apple-and-orange/problem"

# import numpy as np
import math
import os
import random
import re
import sys

def isInHouse(x, s, t):
    """
    check if x in s t
    :param x: apple or organ
    :param s:
    :param t:
    :return:
    """
    if x >= s and x <= t:
        return True
    else:
        return False

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    """

    :param s: home start
    :param t: home end
    :param a: apple tree root
    :param b: orange tree root
    :param apples: distance of apple
    :param oranges: distance of orange
    :return:
    """


    # distance from home to apple tree (a to s) and home to orange tree (t to b)
    d_home_apple = s - a
    d_home_orange = b -t

    # apples = np.array(apples)
    # napple = len(apples[apples>=d_home_apple])
    # norange = len(oranges[oranges<= -d_home_orange])

    in_house_apple = [ap for ap in apples if isInHouse(ap+a,s,t) ]
    in_house_organe = [o for o in oranges if isInHouse(o+b, s, t)]

    print(len(in_house_apple))
    print(len(in_house_organe))


def submit():
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)



if __name__ == '__main__':
    submit()


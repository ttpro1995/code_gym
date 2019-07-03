#!/bin/python3

__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"
__url__ = "https://www.hackerrank.com/challenges/utopian-tree/problem"


import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    # 0 is spring, double
    # 1 is summer, + 1
    flag = 0
    total = 1
    for i in range(n):
        if flag is 0:
            total *= 2
            flag = 1
        else:
            total += 1
            flag = 0
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"

__link__ = "https://codingcompetitions.withgoogle.com/codejam/round/0000000000000130/0000000000000523"

from googlecodejam.google_interactive import readline, readline_int, readline_two_int

import sys

def get_mid_value(a, b):
    mid = (b - a) // 2 + 1
    mid_value = a + mid
    return mid_value


def process_test_case():
    a, b = readline_two_int()
    n = readline_int()

    answer = None

    while (True):
        mid_value = get_mid_value(a, b)
        print(mid_value)
        answer = input()
        if answer == "WRONG_ANSWER":
            sys.exit(0)
        if answer == "CORRECT":
            return
        if answer == "TOO_SMALL":
            a = mid_value
        if answer == "TOO_BIG":
            b = mid_value-1


if __name__ == "__main__":
    t = readline_int()
    for i in range(t):
        process_test_case()

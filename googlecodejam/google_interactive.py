__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"


def readline_int():
    n = input()
    return int(n)


def readline_two_int():
    line = input()
    tok = line.split(" ")
    a = int(tok[0])
    b = int(tok[1])
    return a, b


def readline():
    return input()

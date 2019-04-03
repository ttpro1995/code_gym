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

def readline_int_list():
    toks = readline().split(" ")
    toks = list(map(int, toks))
    return toks


if __name__ == "__main__":
    arr = readline_int_list()
    for i in arr:
        print(i+1)

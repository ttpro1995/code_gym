__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"


def rightTriangle(sides):
    ssides = sorted(sides)
    hh = ssides[2]*ssides[2]
    ss = ssides[0]*ssides[0] + ssides[1]*ssides[1]
    if ss == hh:
        return True
    else:
        return False

x = [3,5,4]

xs = sorted(x)

print(xs)


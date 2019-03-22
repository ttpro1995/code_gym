# __name__ = "Thai Thien"
#
# __link__ = "https://app.codesignal.com/challenge/7kZavbM3FBC85FtNA"
__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"

def isSmooth(arr):
    """
    An array is called smooth if its first and its last elements are equal to one another and to the middle
    :param arr: the array of int
    :return: true if arr is smooth
    """

    size = len(arr)
    if size % 2 == 0: # even case
        mid1 = arr[(int)(size/2)-1]
        mid2 = arr[(int)(size/2)]
        mid = mid1 + mid2
    else:
        mid = arr[(int)(size/2)]
    start = arr[0]
    end = arr[-1]
    if (end == start) and (end == mid):
        return True
    return False




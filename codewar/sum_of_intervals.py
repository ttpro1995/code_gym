def sum_of_intervals(interval):
    # sort interval
    interval_sorted = sort_interval(interval)
    # print(interval_sorted)
    interval_merged = merge_all_overlap(interval_sorted)
    # print(interval_merged)
    interval_length = [interval_len(i) for i in interval_merged]
    return sum(interval_length)


def is_interval_overalap(a, b):
    """
    check if b start in the interval of a
    :param a: interval as list size of two, a start before b
    :param b: interval as list size of two
    :return: True or False
    """

    if (a[0] <= b[0]) and (a[1] >= b[0]):
        return True
    return False


def merge_two_interval(a, b):
    """
    Merge b to a.
    b start in the inverval of a
    :param a:
    :param b:
    :return:
    """

    if b[1] <= a[1]:
        return a
    elif b[1] > a[1]:
        return [a[0], b[1]]

def get_interval_first(interval):
    return interval[0]

def sort_interval(list_of_interval):
    """

    :param list_of_interval: [[1,2], [1,3]
    :return:
    """
    return sorted(list_of_interval, key=get_interval_first)


def merge_all_overlap(list_of_interval):
    stack = []
    for i in list_of_interval:
        if not stack: # if stack is empty
            # put interval in stack
            stack.append(i)
        else:
            top = stack[-1]
            if is_interval_overalap(top, i):
                top = stack.pop()
                merge_result = merge_two_interval(top, i)
                stack.append(merge_result)
            elif is_interval_overalap(i, top):
                top = stack.pop()
                merge_result = merge_two_interval(i, top)
                stack.append(merge_result)
            else:
                stack.append(i)
    return stack


def interval_len(interval):
    if not interval:
        return 0
    return interval[1] - interval[0]


if __name__ == "__main__":
    print("test merge all overlap")
    a = [
        [1,4],
        [3,8],
        [11, 15],
        [12, 14],
        [10, 12],
        [10, 11]
    ]
    a_sort = sort_interval(a)
    print(a_sort)
    a_merge = merge_all_overlap(a)
    print(a_merge)

    print("test sum")
    b = [
       [1, 5],
       [10, 20],
       [1, 6],
       [16, 19],
       [5, 11]
    ]
    b_sum = sum_of_intervals(b)
    print(b_sum)

    c = [(1, 4), (7, 10), (3, 5)]
    c_sum = sum_of_intervals(c)
    print(c_sum)
__author__ = "Thai Thien"
__link__ = "https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H/description"


def crypt_to_value(single_crypt, solution):
    """
    convert crypt string to value using solution
    :param single_crypt: string
    :param solution: dictionary
    :return:
    """
    value_str = ""
    for ch in single_crypt:
        ch_value = solution[ch]
        value_str += ch_value
    if value_str[0] == '0':
        if len(value_str) > 1:
            return -1
    value = str(value_str)
    return int(value)


def solution_list_to_dict(solution):
    """
    convert solution as list to solution as dict
    :param solution:
    :return:
    """
    so_dict = {}
    for sol in solution:
        so_dict[sol[0]] = sol[1]
    return so_dict


def isCryptSolution(crypt, solution):
    """
    check if crypt 1 + crypt 2 = crypt 3
    :param crypt:
    :param solution:
    :return:
    """
    solution = solution_list_to_dict(solution)
    value1 = crypt_to_value(crypt[0], solution)
    value2 = crypt_to_value(crypt[1], solution)
    result = crypt_to_value(crypt[2], solution)

    if value1==-1 or value2==-1 or result==-1:
        return False

    sum_of_value = value1 + value2
    if sum_of_value == result:
        return True
    else:
        return False


if __name__ == "__main__":
    crypt = ["SEND", "MORE", "MONEY"]
    sols = [["O","0"], ["M","1"], ["Y","2"], ["E","5"], ["N","6"], ["D","7"], ["R","8"], ["S","9"]]
    print(isCryptSolution(crypt, sols))
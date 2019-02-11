#!/bin/python3

__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"
__url__ = "https://www.hackerrank.com/challenges/grading/problem"
__done__ = "OK"


import os
import sys


#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    output = []
    for grade in grades:
        result = rounding_grades(grade)
        output.append(result)
    return output


def rounding_grades(grade):
    """
    round to next multiply of 5
    :param grade:
    :return:
    """
    if grade <= 37:
        return grade
    result = grade
    remain = grade%5
    whole = int(grade/5)*5

    if remain > 0:
        difference = (whole + 5) - grade
        if difference < 3:
            whole += 5
            result = whole
        print(difference)
    return result


def hackerrank_submit():
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

def local_test():
    input_case = [73, 67, 38, 33]
    output_case = gradingStudents(input_case)
    print(output_case)


if __name__ == '__main__':
    hackerrank_submit()

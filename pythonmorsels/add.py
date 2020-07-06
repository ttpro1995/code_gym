problem="""
write a function that 
accepts two lists-of-lists of numbers
 and returns one list-of-lists 
 with each of the corresponding numbers in the two given lists-of-lists added together.
"""
bonus1="""
For the first bonus, modify your add function to accept and "add" any number of lists-of-lists.
"""
bonus2="""
For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape.
"""

link="https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf"


class SquareMatrix:
    def __init__(self, mat):
        self.mat = mat
        check_result = self.check()
        if not check_result:
            raise ValueError("Given matrices are not the same size.")
        self.shape = (len(mat), len(mat[0]))

    def add(self, b):
        if self.shape != b.shape:
            raise ValueError("Given matrices are not the same size.")
        c_mat = [[a+b for a, b in zip(x, y)]
              for x, y in zip(self.mat, b.mat)]
        return SquareMatrix(c_mat)

    def check(self):
        """
        check if matrix is correct, each row or column have same length
        :return:
        """
        count_list = [len(row) for row in self.mat]
        if count_list.count(count_list[0]) == len(count_list):
            return True
        else:
            return False


def test_get_shape():
    print("test_get_shape")
    m1 = SquareMatrix([[1, -2], [-3, 4]])
    print(m1.shape)


def test_plus():
    print("test_plus")
    m1 = SquareMatrix([[1, -2], [-3, 4]])
    m2 = SquareMatrix([[2, -1], [0, -1]])
    m3 = m1.add(m2)
    print(m3.mat)


def test_list_plus():
    print("test_list_plus")
    matrix1 = [[1, 9], [7, 3]]
    matrix2 = [[5, -4], [3, 3]]
    matrix3 = [[2, 3], [-3, 1]]
    # m1 = SquareMatrix(matrix1)
    # m2 = SquareMatrix(matrix2)
    # m3 = SquareMatrix(matrix3)
    result = add(matrix1, matrix2, matrix3)
    print(result)


def test_raise_error():
    print("test_raise_error")
    add([[1, 9], [7, 3]], [[1, 2], [3]])


def test():
    test_get_shape()
    test_plus()
    test_list_plus()
    test_raise_error()

# function to solve problem


def add_1(mat1, mat2):
    m1 = SquareMatrix(mat1)
    m2 = SquareMatrix(mat2)
    return m1.add(m2).mat


def add(*list_of_mat):
    m= SquareMatrix(list_of_mat[0])
    for m_other in list_of_mat[1:]:
        m = m.add(SquareMatrix(m_other))
    return m.mat


if __name__ == "__main__":
    test()
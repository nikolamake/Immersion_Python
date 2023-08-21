import pytest
@pytest.fixture
def mat1():
    return [[1, 2, 9], [5, 6, 11], [7, 8, 6]]
@pytest.fixture
def mat2():
    return [[3, 4, 7], [10, 12, 12],  [7, 1, 11]]


def sum_(self: list, other: list):
    """Сложение двух матриц"""
    res = []
    for i in range(len(self)):
        sub_res = []
        for j in range(len(self[0])):
            sub_res.append(self[i][j] + other[i][j])
        res.append(sub_res)
    return res

def eq_(self, other):
    """Сравнение двух матриц"""
    for i in range(len(self)):
        for j in range(len(self[0])):
            if self[i][j] != other[i][j]:
                return False
    return True

def mul_(self, other):
    """Умножение двух матриц"""
    res = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*other)] for row_a in self]
    return res

def test_sum(mat1, mat2):
    assert sum_(mat1, mat2) == [[4, 6, 16], [15, 18, 23], [14, 9, 17]]

def test_mul(mat1, mat2):
    assert mul_(mat1, mat2) == [[86, 37, 130], [152, 103, 228], [143, 130, 211]]
def test_eq(mat1, mat2):
    assert eq_(mat1, mat2) == False


if __name__ == '__main__':
    pytest.main(['-v'])
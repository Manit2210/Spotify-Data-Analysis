"""
File read the spotify revenue csv file
"""
import csv
import statistics


def read_csv(str1: str, str2: str, str3: str) -> dict[str: (int, int, int)]:
    """
    Read the revenue, users, and subscription csv files
    """
    dict1 = {}
    with open(str1) as file:
        reader = csv.reader(file, delimiter=',')
        for _ in range(5):
            next(reader)
        for row in reader:
            dict1[row[0]] = int(row[1])
    dict2 = {}
    with open(str2) as file:
        reader = csv.reader(file, delimiter=',')
        for _ in range(9):
            next(reader)
        for row in reader:
            dict2[row[0]] = int(row[1])
    dict3 = {}
    with open(str3) as file:
        reader = csv.reader(file, delimiter=',')
        for _ in range(9):
            next(reader)
        for row in reader:
            dict3[row[0]] = int(row[1])
    l1 = [dict1[items] for items in dict1]
    l2 = [dict2[items] for items in dict2]
    l3 = [dict3[items] for items in dict3]
    dict4 = {}
    for item in dict1:
        for i in range(len(l1)):
            if dict1[item] == l1[i]:
                dict4[item] = (l1[i], l2[i], l3[i])
    return dict4


def find_rsquare_matrix(dict1: dict[str: (int, int, int)]) -> list[list[float, float], list[float, float]]:
    """
    Find R for the spotify_revenue file
    """
    list_of_items = [dict1[item] for item in dict1]
    lp1 = []
    lp2 = []
    lr = []
    for item in list_of_items:
        lp1.append(item[1])
        lp2.append(item[2])
        lr.append(item[0])
    avg_x1 = statistics.mean(lp1)
    avg_x2 = statistics.mean(lp2)
    avg_y = statistics.mean(lr)
    n1 = 0
    n2 = 0
    n3 = 0
    d11 = 0
    d21 = 0
    d31 = 0
    d12 = 0
    d22 = 0
    d32 = 0
    for i in range(len(lp1)):
        n1 = n1 + (lp1[i] - avg_x1) * (lr[i] - avg_y)
        n2 = n2 + (lp2[i] - avg_x2) * (lr[i] - avg_y)
        n3 = n3 + (lp2[i] - avg_x2) * (lp1[i] - avg_x1)
        d11 = d11 + (lp1[i] - avg_x1) ** 2
        d21 = d21 + (lp2[i] - avg_x2) ** 2
        d31 = d31 + (lp2[i] - avg_x2) ** 2
        d12 = d12 + (lr[i] - avg_y) ** 2
        d22 = d22 + (lr[i] - avg_y) ** 2
        d32 = d32 + (lp1[i] - avg_x1) ** 2

    r1 = n1/((d11 * d12)**0.5)
    r2 = n2/((d21 * d22)**0.5)
    r3 = n3/((d31 * d32)**0.5)

    r1 = r1 ** 2
    r2 = r2 ** 2
    r3 = r3 ** 2

    return [[r1, 0], [r2, r3]]


def r_square(lst: list[tuple[float, float], tuple[float, float]]) -> float:
    """
    Function to find total value for r^square for the whole model
    """
    r1 = lst[0][0]
    r2 = lst[1][0]
    r3 = lst[1][1]
    rx1y = r1 ** 0.5
    rx2y = r2 ** 0.5
    rx2x1 = r3 ** 0.5
    transpose = calculate_transpose([[rx1y], [rx2y]])
    inverse = calculate_inverse([[1, rx2x1], [rx2x1, 1]])
    m1 = multiply_matrix(transpose, inverse)
    r2 = multiply_matrix(m1, [[rx1y], [rx2y]])
    return r2[0][0]


def calculate_transpose(lst: list[list[float]]) -> list[list[float]]:
    """This function calculates the transpose of a matrix. Each row in the matrix should be a
    list within the list
    """
    new_row = len(lst)
    new_colowm = len(lst[0])
    l1 = []
    for i in range(new_colowm):
        l2 = []
        l1.append(l2)
        for j in range(new_row):
            l2.append(lst[j][i])
    return l1


def calculate_inverse(lst: list[list[float, float], list[float, float]]) -> list[list[float]]:
    """
    The function calculates the inverse of a 2 by 2 matrix. The argument should be of a 2 by 2
    matrix as well
    """
    a, b = lst[0][0], lst[0][1]
    c, d = lst[1][0], lst[1][1]
    determinant = 1/((a * d) - (b * c))
    new_matrix_row1 = [determinant * d, determinant * -b]
    new_matrix_row2 = [determinant * -c, determinant * a]
    return [new_matrix_row1, new_matrix_row2]


def multiply_matrix(lst1: list[list[float]], lst2: list[list[float]]) -> list[list[float]]:
    """
    The function multiplies two matrices where lst1 is the first matrix and lst2 is the second. The
    order MATTERS

    Preconditions:
    - len(lst1[0]) == len(lst2)
    """
    res = [[0 for _ in range(len(lst2[0]))] for _ in range(len(lst1))]
    for i in range(len(lst1)):
        for j in range(len(lst2[0])):
            for k in range(len(lst2)):
                res[i][j] += lst1[i][k] * lst2[k][j]

    return res

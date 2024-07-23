#!/usr/bin/python3
''' working with Pascal's triangle.
'''


def pascal_triangle(a):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(a) is not int or a <= 0:
        return triangle
    for i in range(a):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle

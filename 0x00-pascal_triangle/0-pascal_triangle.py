
#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""

from math import factorial
def NCR(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(NCR(i, j))
        triangle.append(row)
    return triangle

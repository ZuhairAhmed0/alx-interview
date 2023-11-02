#!/usr/bin/python3
""" N queens """
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
except ValueError:
    print("N must be a number")
    exit(1)


def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """ solve """
    for solution in queens(n, 0):
        k = [[i, s] for i, s in enumerate(solution)]
        print(k)


solve(n)

# https://www.hackerrank.com/contests/moodys-analytics-2018-university-codesprint/challenges/meeting-profit-target
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(profits):
    entries = len(profits)
    i = 0
    for transaction_list in profits:
        if i < entries - 1:
            if transaction_list[0] < transaction_list[1]:
                profits[i + 1][1] = profits[i + 1][1] + (transaction_list[1] - transaction_list[0])
        else:
            if transaction_list[0] < transaction_list[1]:
                print('0')
                return 1
            else:
                print('1')
                return 0
        i += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        profits = []

        for _ in range(n):
            profits.append(list(map(int, input().rstrip().split())))

        res = solve(profits)

        fptr.write(str(res) + '\n')

    fptr.close()

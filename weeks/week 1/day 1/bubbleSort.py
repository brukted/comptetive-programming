#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(arr):
    # Write your code here
    is_sorted = False
    iterations = 0
    swaps = 0
    while(not is_sorted):
        is_sorted = True
        for i in range(1, len(arr)-iterations):
            if(arr[i-1] > arr[i]):
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swaps += 1
                is_sorted = False
        iterations = iterations + 1
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(arr[0]))
    print('Last Element: {}'.format(arr[-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

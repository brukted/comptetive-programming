#!/bin/python3

# https://www.hackerrank.com/challenges/insertionsort1/problem

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(n, arr):
    # Write your code here
    for i in range(n-1, 0, -1):
        temp = arr[i]
        if temp < arr[i-1]:
            arr[i] = arr[i-1]
            for j in range(n):
                print(arr[j], end=" ")
            print()
            arr[i-1] = temp
        if i == 1:
            for j in range(n):
                print(arr[j], end=" ")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

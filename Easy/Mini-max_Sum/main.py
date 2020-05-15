#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    small = min(arr)
    big = max(arr)
    sum = 0
    for num in arr:
        sum+=num
    print(sum-big, sum-small)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    l = len(arr)
    sum1,sum2 = 0,0
    for i in range(0,l):
        sum1 += arr[i][i]
    index = 0
    for i in range(l,0,-1):
        sum2 +=arr[index][i-1]
        index+=1
    return abs(sum1-sum2)

        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

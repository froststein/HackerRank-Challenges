#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for z in range(i,j+1):
        tmp1 = int(str(z)[::-1])
        if (abs(tmp1-z)) % k == 0:
            count+=1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

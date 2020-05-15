#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    tmp=[]

    for n in range(max(a),min(b)+1):
        cond = True
        for numI in a:
            if(n < numI):
                if numI % n != 0 :
                    cond=False
            else:
                if n % numI != 0:
                    cond=False
        for numK in b:
            if(n < numK):
                if numK % n != 0 :
                    cond=False
            else:
                if n % numK != 0:
                    cond=False
        if(cond):
            tmp.append(n)

    return len(tmp)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)
    #fptr.write(str(total) + '\n')

    #fptr.close()

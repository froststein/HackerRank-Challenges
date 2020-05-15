#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    dictMin = {}
    diff = 0
    dffArr =[]
    for i in range(0,len(a)):
        if(a[i] in dictMin):
            diff = i - dictMin[a[i]]
            dffArr.append(diff)
        else:
            dictMin[a[i]]=i
    if(len(dffArr) != 0 ):
        return min(dffArr)
    else:
        return -1
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

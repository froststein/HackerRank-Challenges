#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    pos, val = 0,0
    for i in range(0,n):
        if (s[i] == 'U'):
            pos +=1
            if(pos == 0):
                val += 1
        else:
            pos -=1
        print(l,pos)
    return val

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

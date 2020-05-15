#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    big, occ = 0,0
    for can in ar:
        if(can == big):
            occ+=1
        if(can > big):
            big = can
            occ = 1
    return occ

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

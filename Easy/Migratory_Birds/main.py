#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    tmp = [0,0,0,0,0]
    for i in range(0,len(arr)):
        tmp[arr[i]-1] += 1
    return tmp.index(max(tmp))+1

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

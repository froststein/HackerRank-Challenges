#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    total = 0
    shared = 5
    for i in range(1,n+1):
        shared = int(shared/2)
        total += shared
        shared *=3
    return total

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)
    print(result)
    #fptr.write(str(result) + '\n')

    #3fptr.close()

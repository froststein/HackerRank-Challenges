#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ascore,bscore = 0,0
    for i in range(0,3):
        if(a[i] != b[i]):
            if(a[i]>b[i]):
                ascore+=1
            else:
                bscore+=1
    return [ascore,bscore]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

   # fptr.close()

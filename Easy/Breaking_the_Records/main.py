#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minS,maxS = scores[0],scores[0]
    minCount,maxCount = 0,0
    for score in scores:
        if score > maxS:
            maxS = score
            maxCount += 1
        if(score < minS):
            minS = score
            minCount += 1
    
    return [maxCount,minCount]


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()

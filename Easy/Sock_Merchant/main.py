#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    checkPair = []
    numPair = 0
    for i in range(0,len(ar)):
        k = i+1
        count = 1
        while k < len(ar):
            if(ar[i] in checkPair):
                break
            else:
                print(ar[i],ar[k])
                if(ar[i] == ar[k]):
                    count+=1
            k += 1
        checkPair.append(ar[i])
        numPair += int(count/2)
    return numPair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

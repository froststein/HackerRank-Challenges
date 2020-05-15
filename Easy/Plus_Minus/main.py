#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zero,pos,neg = 0,0,0
    for num in arr:
        if(num == 0):
            zero += 1
        elif(num > 0):
            pos += 1
        elif(num < 0):
            neg += 1
    div = len(arr)
    print('{0:.6f}'.format(pos/div))
    print('{0:.6f}'.format(neg/div))
    print('{0:.6f}'.format(zero/div))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

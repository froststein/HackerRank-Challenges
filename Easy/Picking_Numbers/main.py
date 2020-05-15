#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    dic = {}
    for num in a:
        dic[num] = dic.get(num, 0) + 1
        dic[num+1] = dic.get(num+1, 0) + 1
    return max(dic.values())

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    maxTotal = 0
    for i in range(0,len(keyboards)):
        k = 0
        while k < len(drives):
            total = keyboards[i]
            total+=drives[k]
            if( total <= b and total > maxTotal):
                maxTotal = total
            k += 1
    if(maxTotal == 0):
        return -1
    else:
        return maxTotal

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
    #fptr.write(str(moneySpent) + '\n')

    #fptr.close()

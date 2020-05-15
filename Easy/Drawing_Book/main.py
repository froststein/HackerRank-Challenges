#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    f1,f2 = 0,1
    if(n%2 == 0):
        b1,b2 = n,0
    else:
        b1,b2 = n-1,n
    front,back = False,False
    countF,countB = 0,0
    while True:
        if(not front):
            if(f1 == p or f2 == p):
                front = True
            else:
                f1 += 2
                f2 += 2
                countF+=1
        if(not back):
            if(b1 == p or b2 == p):
                back = True
            else:
                b1 -= 2
                b2 = b1 +1 
                countB+=1
        if(front and back == True):
            break
    print(countF,countB)
    return min([countF,countB])
    

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    #fptr.write(str(result) + '\n')

    #fptr.close()

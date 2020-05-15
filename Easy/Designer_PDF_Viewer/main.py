#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    b = 0
    for l in word:
        if(int(h[ord(l)-97]) > b):
            b=h[ord(l)-97]
    return len(word)*b

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()

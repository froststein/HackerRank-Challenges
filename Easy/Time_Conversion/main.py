#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time = s.split(":")
    tmp = []
    if s[-2:] == "PM":
        if time[0] != "12":
            tmp.append(str(int(time[0])+12))
    else:
        if time[0] == "12":
            tmp.append('00')
    tmp.append(time[1])
    tmp.append(time[2])
    ctime = ':'.join(tmp)
    return str(ctime[:-2])

if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    #f.write(result + '\n')

    #f.close()

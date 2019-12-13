#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    index = 0
    while index < n:
        #同じペアがあったらカウント
        if ar[index] == ar[index + 1]:
            count += 1
            index += 2
        else:
            #等しくなければindexを進める
            index += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

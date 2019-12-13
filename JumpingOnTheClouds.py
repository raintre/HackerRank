#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n, c):
    count = current = 0
    end = len(c) - 1
    while current < end:
        if current + 2 <= end and c[current + 2] == 0:
            current += 2
            count  += 1
        elif c[current + 1] == 0:
            current += 1
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()

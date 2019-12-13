#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def array_left_rotation(n, d, a):
    return a[d:]+a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = array_left_rotation(n, d, a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

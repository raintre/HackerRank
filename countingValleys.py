#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	piv = valley = 0
	for index in range(n):
		if s[index] == 'U':
			piv += 1
			if piv == 0:
				valley += 1
		else:
			piv -= 1
	return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

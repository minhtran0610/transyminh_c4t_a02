import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    a = arr[n-1]
    for i in range (n-2,-1,-1):
        if arr[i] < a:
            arr[i+1] = a
            a = arr[i]
            for i in range (n):
                if i < n-1:
                    print(arr[i], end=' ')
                else:
                    print(arr[i])
        else:
            arr[i+1] = arr[i]
            for i in range (n):
                if i < n-1:
                    print(arr[i], end=' ')
                else:
                    print(arr[i])
  
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
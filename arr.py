import math
import os
import random
import re
import sys
def flippingMatrix(matrix):
    # Write your code here
    l=len(matrix)
    print(l)
    print(matrix)
    for  i in range(l):
        k=0
        for j in range(l):
            if j ==2:
                matrix[i][j],matrix[l-k-1][j]=matrix[l-k-1][j], matrix[i][j]
                k+=1
                breakpoint
    
    for i in matrix:
        for j in matrix:
            if i==0:
                k=0
                while k<=l:
                    a[i][j],a[i][l-k]=a[i][l-k], a[i][j]
    print(matrix)
    sum = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix)//2):
            sum +=matrix[i][j]
            

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

    print(result)


# 112 42 83 119
# 56 125 56 49
# 15 78 101 43
# 62 98 114 108
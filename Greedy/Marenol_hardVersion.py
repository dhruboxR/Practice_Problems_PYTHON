# https://codeforces.com/problemset/problem/2254/C2

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    a = input().strip()
    b = input().strip() 

    # store the indices of 1's for both strings then sum up the distance 
    # operation moves 2 steps at a time , so move = totalSum / 2

    move = 0

    for i in range(2) : 
        idxA = []
        idxB = []

        for j in range(i, n, 2) : 
            if a[j] == '1' : idxA.append(j)
            if b[j] == '1' : idxB.append(j) 

        # there must be equal number of 1's present in both string 
        if len(idxA) != len(idxB) :
            print( "-1" )
            return 

        # sum up the distance 
        for j in range(len(idxA)) : move += abs(idxA[j] - idxB[j]) 

    print( move//2 )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
# https://codeforces.com/problemset/problem/2259/C

import sys
import math
input = sys.stdin.readline

"""
    MARK THE FIRST ONE, MARK THE LAST ONE 
            The rest in the middle becomes -> 0 
"""

def solve():
    n = int( input())
    vect = list(map(int, input().split()))

    for i in range(n) :
        if vect[ i ] == -1 : 
            vect[ i ] = 1
        if vect[ i ] == 1 : break

    for i in range(n-1, -1, -1) : 
        if vect[ i ] == -1 : 
            vect[ i ] = 1
        if vect[ i ] == 1 : break

    print( *(max(val, 0) for val in vect) )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
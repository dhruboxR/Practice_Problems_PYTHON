# https://codeforces.com/problemset/problem/2244/C

import sys
import math
input = sys.stdin.readline

"""
    Sorting is always possible if difference % gcd == 0 

        difference = (final position - initial position)
        gcd = gcd(x, y)
"""

def solve():
    n, x, y = map(int, input().split()) 
    values =  list(map(int, input().split())) 

    gc = math.gcd(x, y)

    for i in range(n) : 
        if values[i] != i+1 : 
            # not in the correct position 
            diff = abs(values[i] - (i+1))

            if diff % gc != 0 :
                print( "no" )
                return 

    print( "yes" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
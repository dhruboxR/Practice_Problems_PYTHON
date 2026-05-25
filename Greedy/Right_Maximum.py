# https://codeforces.com/contest/2204/problem/B

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    moveCounter = 0
    mx = -1
    for i in range(length) :
        mx = max(mx, source[ i ])

        if mx == source[ i ] :
            moveCounter += 1
    
    print( moveCounter )


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
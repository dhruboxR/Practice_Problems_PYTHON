# https://codeforces.com/contest/2224/problem/A

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    len = int(input())
    source = list( map(int, input().split()) )

    counter = store = 0
    if source[ len-1 ] > 0 : counter += 1

    for i in range(len-2, -1, -1) :
        if source[ i ] + source[ i+1 ] > 0 and source[ i ] + source[ i+1 ] > source[ i ] :
            source[ i ] += source[ i+1 ]
        if source[ i ] > 0 : counter += 1

    print( counter )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
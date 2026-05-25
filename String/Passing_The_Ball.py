# https://codeforces.com/contest/2204/problem/A

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    length = int( input() )
    sequence = input().strip()

    counter = 0
    for i in range(length) :
        counter += 1
        if sequence[ i ] == 'L' : break
    
    print( counter )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
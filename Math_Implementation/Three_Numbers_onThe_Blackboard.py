# https://codeforces.com/contest/2256/problem/A

import sys
import math
input = sys.stdin.readline

def solve():
    src = list(map(int, input().split())) 
    src.sort()

    if src[ 2 ] > src[ 0 ] + src[ 1 ] : src[ 2 ] = src[ 0 ] + src[ 1 ]
    print(src[ 2 ] - src[ 0 ])

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
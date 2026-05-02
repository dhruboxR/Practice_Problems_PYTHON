# https://codeforces.com/contest/2227/problem/A

import sys
input = sys.stdin.readline

def solve():
    cx, cy = map(int, input().split())
    if (cx&1) and (cy&1) :
        # both are odd numbers not possible 
        print( "NO" )

    else : print( "YES" )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
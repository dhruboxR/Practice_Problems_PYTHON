# https://codeforces.com/contest/2225/problem/A

import sys
input = sys.stdin.readline

def solve():
    x, y = map(int, input().split() )
    mxMultiple = ((y - 1) // x) * x

    if (mxMultiple < y and mxMultiple > x) and (y % mxMultiple != 0) :
        print( "YES" ) 
    else :
        print( "NO" ) 

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
# https://codeforces.com/contest/2244/problem/A

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    string = input().strip()

    mlen = curr = 0 
    for i in range(n) :
        if string[ i ] == '#' : curr += 1 
        else : 
            mlen = max(mlen, curr) 
            curr = 0
    mlen = max(mlen, curr) 

    print( ((mlen//2)+1) if mlen&1 else mlen//2 )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
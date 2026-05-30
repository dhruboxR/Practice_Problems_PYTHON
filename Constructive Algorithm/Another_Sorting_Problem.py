# https://codeforces.com/contest/2231/problem/B

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    # what is the maximum k that is needed for a single element
    k = 0 
    for i in range(1, length) :
        if source[ i ] < source[ i-1 ] :
            k = max(k, source[ i-1 ] - source[ i ])
    
    for i in range(1, length) :
        if source[ i ] < source[ i-1 ] :
            if source[ i ] + k < source[ i-1 ] :
                print( "NO" )
                return
            
            source[ i ] += k
    
    print( "YES" )


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
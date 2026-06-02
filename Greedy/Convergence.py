# https://codeforces.com/contest/2232/problem/A

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

# BRUTEFORCE O(n2)
#   Consider each position as the target position, then count
#       a - the number of elements less than current 
#       b - the number of elements greater than current 
# Minimum calls needed for all others to come to this position is max(a,b)

def solve():
    len = int( input() )
    source = list( map(int, input().split()) )
    source.sort()

    finCall = 10**9
    for i in range(len) :
        currentCall = lower = higher = 0
        
        for j in range(len) :
            if source[ j ] > source[ i ] : higher += 1
            if source[ j ] < source[ i ] : lower += 1
        
        currentCall = max(lower, higher)
        finCall = min(finCall, currentCall)

    print( finCall ) 

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
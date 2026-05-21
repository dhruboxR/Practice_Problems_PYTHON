# https://codeforces.com/contest/1669/problem/H

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

    # The optimal strategy is to take the highest bit, 
    # such that we have enough moves to set that bit in every element

def solve():
    length, move =  map(int, input().split())

    source = list( map(int, input().split()) )
    bitTrack = [0] * 31

    for intValue in source :
        # check in which positions the bits are set in this number
        for i in range(30, -1, -1) :
            if intValue & (1 << i) : bitTrack[ i ] += 1
    
    finalAnd = 0

    for i in range(30, -1, -1) :
        # moves needed to set this bit in every number
        moveNeeded = length - bitTrack[ i ]

        if moveNeeded <= move :
            move -= moveNeeded
            finalAnd += ( 1 << i )
    
    print( finalAnd )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
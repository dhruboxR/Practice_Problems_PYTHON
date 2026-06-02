# https://codeforces.com/contest/520/problem/B

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

# Reverse approach : From Target -> Current

def solve():
    current, target = map(int, input().split())
    
    # If starting number is already greater then doubling is useless
    if current >= target : print( current - target )
    else :
        # try to reach as close as possible while target > current [ divide by 2 ]
        move = 0
        while target > current :
            if target&1 : target += 1
            else : target //= 2
            move += 1
        # target might go below current 
        move += current - target
        print( move )

solve()
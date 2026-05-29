# https://codeforces.com/contest/2211/problem/B

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    diff = abs(a - b)

    if a == b : 
        print( 1 )
    else :
        # if the sum = abs(a - b), then the number of equalSum partition
        # Is equal to the number of divisor of s
        divisor = 0
        for i in range(1, diff+1) :
            if diff % i == 0 : divisor += 1

        print( divisor )

    for _ in range(a) : print('1', end = ' ')
    for _ in range(b) : print('-1', end = ' ')

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
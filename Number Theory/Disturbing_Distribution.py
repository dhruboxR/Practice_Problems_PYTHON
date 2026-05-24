# https://codeforces.com/problemset/problem/2226/A

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    total = 0
    for i in range(length) :
        if source[ i ] == 1 :
            if i == length-1 : total += 1
            else : i += 1
        else : total += source[ i ]
        
    print( total )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
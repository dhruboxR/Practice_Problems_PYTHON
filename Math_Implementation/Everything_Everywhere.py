# https://codeforces.com/problemset/problem/2226/B

import sys
import math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    total = 0
    for i in range(1, length) :
        sub = abs(source[ i ] - source[ i-1 ])
        gc = math.gcd(source[ i ], source[ i-1 ]) 

        if gc == sub : total += 1
        
    print( total )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
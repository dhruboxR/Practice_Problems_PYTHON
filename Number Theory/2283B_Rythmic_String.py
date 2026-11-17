# https://codeforces.com/contest/2283/problem/B

import sys
import math
input = sys.stdin.readline
"""
    muiltiple numbers can only maintain the RYTHM if and only if their GCD is same 
        n <= 5000 (n2 solution is acceptable)

    - find the number with maximum number of multiples present in the array 
    - remove the rest 
"""
def solve():
    n = int( input() )
    source = list(map(int, input().split())) 

    mxMultiple = 0
    for i in range(n) : 
        curr = source[i]
        mul = 0
        for j in range(n) : 
            if source[j] % curr == 0 : 
                mul += 1

        mxMultiple = max(mxMultiple, mul)

    print(n - mxMultiple)

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
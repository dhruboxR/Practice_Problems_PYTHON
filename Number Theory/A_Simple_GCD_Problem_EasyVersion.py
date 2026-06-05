# https://codeforces.com/problemset/problem/2210/C1

import sys
input = sys.stdin.readline
from math import gcd, lcm

def solve():
    length = int( input() )

    a = list( map(int, input().split()) )
    b = list( map(int, input().split()) )

    ans = (a[0] != gcd(a[0], a[1])) + (a[-1] != gcd(a[-1], a[-2]))

    for i in range(1, length-1) :
        left_gcd = gcd(a[ i ], a[ i-1 ])
        right_gcd = gcd(a[ i ], a[ i+1 ])

        multiple = lcm(left_gcd, right_gcd)

        ans += (multiple != a[ i ])
    
    print( ans )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
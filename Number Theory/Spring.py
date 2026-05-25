# https://codeforces.com/contest/2204/problem/C

import sys
import math
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    a, b, c, d = map( int, input().split() )

    alice = ((d // a) * 6) - ((d // math.lcm(a,b)) * 3) - ((d // math.lcm(a,c)) * 3) + ((d // math.lcm(math.lcm(a,b), c)) * 2)
    bob = ((d // b) * 6) - ((d // math.lcm(a,b)) * 3) - ((d // math.lcm(b,c)) * 3) + ((d // math.lcm(math.lcm(a,b), c)) * 2)
    carol = ((d // c) * 6) - ((d // math.lcm(a,c)) * 3) - ((d // math.lcm(b,c)) * 3) + ((d // math.lcm(math.lcm(a,b), c)) * 2)

    print( alice, bob, carol )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

# largest common multiple 
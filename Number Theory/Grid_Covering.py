# https://codeforces.com/problemset/problem/2217/C

import sys
import math
input = sys.stdin.readline

def solve():
    n, m, a, b = map(int, input().split())

    # must be coprime with respective dimensions
    if math.gcd(n,a) != 1 or math.gcd(m,b) != 1 or math.gcd(n,m) > 2 : print( "NO" )
    else : print( "YES" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()


# A must be coprime with N  :  gcd(N,A) = 1
# B must be coprime with M  :  gcd(M,B) = 1

# gcd(N,M) must be at most 2 : gcd(N,M)≤2

#     If gcd(N,M) = 1: there is 1 group → all cells can be visited.
#     If gcd(N,M) = 2: there are 2 groups → alternation lets us visit both groups.

#     If gcd(N,M) > 2: there are more than 2 groups, 
#     but we can visit at most 2 of them → some cells are never reached.
# 
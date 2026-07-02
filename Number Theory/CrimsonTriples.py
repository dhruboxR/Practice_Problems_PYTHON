# https://codeforces.com/problemset/problem/2238/B

import sys
input = sys.stdin.readline

"""
gcd(lcm(a,b),lcm(b,c)) = gcd(a,c)
-  if we can make lcm(a, b) = a AND lcm(b, c) = c Then we can make gcd(a, c) = gcd(a, c)
-       THIS CONTIDITION IS ONLY POSSIBLE WHEN A AND C BOTH ARE DIVISIBLE BY B 

SO FOR A CERTAIN RANGE X :
-   we have florr(x / b) multiples of B 

-    CHOICES FOR a = floor(x/b)
-    CHOICES FOR b = florr(x/b) 

so at each iteration we get squared number of wyas 
"""

def solve():
    bound = int( input() )

    nWays = 0;
    for b in range(1, bound+1) : 
        mulInBound = (bound // b)
        
        # BASE ** EXPONENT [ syntax ]
        nWays += mulInBound ** 2
    
    print( nWays )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
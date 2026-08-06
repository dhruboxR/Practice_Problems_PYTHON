# https://codeforces.com/problemset/problem/2247/B
import sys
import math
input = sys.stdin.readline

"""
 -  The construction is not possible if subarray len (k) > divisor (m)

 -  the solution is to make aj=1 for all j such that 
        -   j mod k ≠ 0, and 
        -   aj = (m − k + 1) for [ j mod k ≡ 0 ]

        In this construction, every subarray of length k has the sum of exactly m, 
        and every subarray whose length is less than k obviously has a sum that is greater than 0
        and less than m, therefore it can't be divisible by m
"""
def solve():
    n, k, m = map(int, input().split()) 
    if k > m : 
        print( "no" )
        return

    print( "yes" )
    for i in range(1, n+1) : 
        if i % k == 0 : 
            print(m - k + 1, end = ' ')
        else : 
            print('1', end = ' ')
    print()

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
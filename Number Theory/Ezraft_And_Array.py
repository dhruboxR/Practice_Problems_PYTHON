# https://codeforces.com/contest/2246/problem/B

import sys
import math
input = sys.stdin.readline

ans = [1, 2, 3]
while( len(ans) < 50 ) : ans.append( ans[-1]*2 )

def solve():
    n = int( input() ) 
    if n == 2 : 
        print( -1 ) 
        return
    
    # print till n 
    print( *ans[:n] )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

"""
Problem:
    Construct an array of n distinct positive integers such that
    the sum of all elements is divisible by every element.

Observation:
    Let S = a1 + a2 + ... + an.
    We need every ai to be a divisor of S.

Special Case:
    n = 2 is impossible.
    If a + b = S and both a and b divide S:
        a | (a+b) => a | b
        b | (a+b) => b | a
    Therefore a and b must be equal, but elements must be distinct.
    Hence answer is -1.

Construction:
    Use the sequence:
        1, 2, 3, 6, 12, 24, ...

    Initially:
        1 + 2 + 3 = 6
    All numbers divide the sum.

    After adding a number x:
        Current sum = 2*x
    Add next number = 2*x
    New sum = 4*x

    Since every previous number divides 2*x,
    they will also divide 4*x.
    The new element 2*x also divides 4*x.

    Therefore the property remains valid for all elements.

Algorithm:
    1. Precompute 50 numbers using:
            1, 2, 3
            next = previous * 2
    2. For each test case:
            if n == 2:
                print -1
            else:
                print first n elements of the sequence
"""
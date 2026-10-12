# https://codeforces.com/contest/2271/problem/A

import sys
import math
input = sys.stdin.readline

"""
        For every single move we must go right then we can either go up or go down 
                - y can never be greater than x+1 [ INVALID ][ NOT POSSIBLE ]
        
        1. Parity same : answer = x
        2. Parity Diff : answer = x+1
"""

def solve():
    a, b = map(int, input().split())

    if b > a+1 : 
        print("-1") 
        return 
    
    if a % 2 == b % 2 : 
        print(a) 
    else : print(a+1) 

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
# https://codeforces.com/problemset/problem/2276/B

import sys
import math
input = sys.stdin.readline

"""
    only 000, 111, 010, 101 these substrings matters 
        - they can appear multiple times but that does not affects the result
        - groupwise check (000, 111) and (010, 101)
"""

def solve():
    string = input().strip() 
    answer = 1 

    if "000" in string or "111" in string : answer += 1
    if "010" in string or "101" in string : answer += 1

    print(answer)

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
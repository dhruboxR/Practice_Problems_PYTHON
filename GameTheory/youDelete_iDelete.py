# https://codeforces.com/problemset/problem/2248/A

import sys
import math
input = sys.stdin.readline

def solve():
    string = input().strip()

    seen0 = False 
    seen1 = False 

    ans = [] 

    for char in string : 
        if char == '0' and not seen0 : 
            seen0 = True 
            continue 
        if char == '1' and not seen1 : 
            seen1 = True 
            continue 

        ans.append(char)

    print(''.join(ans))

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

# STRINGS ARE IMMUTABLE IN PYTHON !! 
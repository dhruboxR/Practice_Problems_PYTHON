# https://codeforces.com/problemset/problem/2250/A
import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    source = list( map(int, input().split()) )

    mn = float('inf')   # minimum on the odd positoins 
    mx = float('-inf')  # maximum on the even positions 

    for i in range(n) : 
        if i % 2 == 0 :                 # 1, 3, 5,...
            mn = min(mn, source[ i ])
        else :                          # 2, 4, 6,...
            mx = max(mx, source[ i ])

    print("YES" if n%2 == 0 and mx + 1 < mn else "NO")
    # n must be even cause every consecutive pair switches positions

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

"""
if wi < k the elemnt at position i moves to i+1
if wi > k the element at position i moves to i-1 
 
so the first element can never move to the left 
& the last element can never move to the right

    - from the odd positions we need the minimun 
    - fromthe even positions we need the maximum 

    k is in between the minimum and the maximum 
    -   so, minimum + 1 < maximum must hold !!  
"""
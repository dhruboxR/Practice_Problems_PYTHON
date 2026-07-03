# https://codeforces.com/contest/2241/problem/C

import sys
input = sys.stdin.readline

def solve():
    n = int( input() )
    s = input().strip()

    """
    IF THERE ARE EXACLY TWO BLOCKS SIDE BY SIDE THEN THE ANSWER IS 2 
        1 1 1 1 0 0 0
        - - - 1 0 - - 
    ELSE THE ANSWER IS 1  
    """
    cnt = 0 
    for i in range(n-1) : 
        if s[ i ] != s[ i+1 ] : cnt += 1
    
    print(2 if cnt == 1 else 1)

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
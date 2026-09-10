# https://codeforces.com/problemset/problem/2254/B

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    str = input().strip()
    len = 1

    # the length after compression, we haven't removed anything yet 
    for i in range(1, n) : 
        if str[ i ] != str[ i-1 ] : len += 1

    ans = len 

    # check for any middle character that connects two blocks 
    for i in range(1,n-1) : 
        if str[ i ] != str[ i-1 ] and str[ i ] != str[ i+1 ] : 
            if str[ i-1 ] == str[ i+1 ] : 
               ans = min(ans, len-2)
            else :
                ans = min(ans, len-1) 

    print(ans)

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
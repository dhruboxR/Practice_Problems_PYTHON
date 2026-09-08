# https://codeforces.com/contest/2260/problem/A

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    source = list(map(int, input().split()))

    zero = source.count(0)      # if the number of zero is < 2 then its not possible 
    if zero < 2 : 
        print(-1) 
        return 

    if source[ 0 ] == 0 and source[ -1 ] == 0 :
        print(0) 
    elif source[ 0 ] == 0 or source[ -1 ] == 0 : 
        print(1) 
    else : print(2) 

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
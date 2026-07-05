# https://codeforces.com/problemset/problem/2241/D

import sys
input = sys.stdin.readline

def solve():
    n = int( input() )
    a = list( map(int, input().split()) )
    b = list( map(int, input().split()) )

    delta = 0 
    for i in range(n) : 
        delta += a[ i ] - b[ i ] 
        if delta > 0 : 
            print( "no" )
            return 
    print( "yes" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

"""
delta += a[ i ] - b[ i ] 

If at any given time delta is greater than 0 
  -  There exists an index i where a[i] > b[i], and the required decrement cannot be balanced 
     by the available addition operations.
"""
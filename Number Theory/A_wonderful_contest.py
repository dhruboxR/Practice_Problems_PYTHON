# https://codeforces.com/problemset/problem/2222/A

import sys
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split() ))

    if 100 in source : print( "yes" )
    else : print( "no" )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
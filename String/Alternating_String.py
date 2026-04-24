# https://codeforces.com/contest/2225/problem/B

import sys
input = sys.stdin.readline

def solve():
    string = input()
    blocks = 0

    for i in range( len(string)-1 ) :
        if string[ i ] == string[ i+1 ] : blocks += 1

    if blocks <= 2 : print( "YES" )
    else : print( "NO" )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
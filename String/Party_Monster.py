# https://codeforces.com/contest/2227/problem/B

import sys
input = sys.stdin.readline

def solve():
    length = int( input() )
    bracketSeq = input().strip()

    lc = rc = 0
    for bracket in bracketSeq :
        if bracket == '(' : 
            lc += 1
        else :
            rc += 1
    
    if abs(lc - rc) != 0 : 
        print( "no" )
    else : 
        print( "yes" )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
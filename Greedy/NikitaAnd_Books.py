# https://codeforces.com/contest/2244/problem/B

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() ) 
    stacks = list( map(int, input().split()) )

    check = []
    for i in range(n) : 
        check.append(i+1)

    store = 0 
    for i in range(n) : 
        if stacks[ i ] > check[ i ] : 
            store += stacks[ i ] - check[ i ]
            stacks[ i ] = check[ i ]
        elif stacks[ i ] < check[ i ] : 
            need = check[ i ] - stacks[ i ]

            if need > store : 
                print( "no" )
                return

            store -= need  
            stacks[ i ] = check [ i ]
    print( "yes" if stacks[-1]+store >= check[-1] else "no" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
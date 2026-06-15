# https://codeforces.com/contest/2197/problem/C

import sys
input = sys.stdin.readline

def solve():
    p, q = map(int, input().split()) 
    if p >= q :
        print( "Alice" )
        return

    diff = q - p
    # bob needs to maintaine this positive diff
    if p >= 2*diff and q >= 3*diff :
        print( "Bob" )
    else : 
        print( "Alice" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

    #    Define: d = y − x ||  Then the target stat  becomes: x = 2d, y = 3d

    #    -So the problem reduces to:
    #         Can the current state still “fit” into a scaled version of the target line?

    #    -Winning region idea

    #   Bob wins if current state is large enough to still reach: (2d,3d)

    #   -So condition: x ≥ 2d and y ≥ 3d means:
    #       The state lies inside a feasible cone leading to the ratio line
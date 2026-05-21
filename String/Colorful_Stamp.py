# https://codeforces.com/contest/1669/problem/D

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    length = int( input() )
    string = input().strip()

    red = False
    blue = False

    for character in string : 
        red |= character == 'R'
        blue |= character == 'B'

        if character == 'W' :
            if (not red and not blue) or (red and blue) :
                red = False
                blue = False
                continue
            else :
                print( "NO" )
                return
    
    if (not red and not blue) or (red and blue) :
        print( "YES" )
    else : print( "NO" )


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

# observation + implementation 
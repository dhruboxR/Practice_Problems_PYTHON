# https://codeforces.com/contest/2259/problem/D

import sys
import math
input = sys.stdin.readline

"""
    If we have 1 zero the answer is NO else the answer is YES

        - two zeros in two different sets : MEX = 1
        - non zero elments in one : MEX = 0

        MEX(A)+MEX(B)+MEX(C) >= 2 * max( MEX(A), MEX(B), MEX(C) )
           1  +  1  +  0     >=   2 * (1)
"""

def solve():
    n = int(input())
    vect = list(map(int, input().split())) 

    z = vect.count(0)

    if z == 1 : 
        print( "no" )
        return 

    print( "yes" )
    z = 0 
    output = [] 

    for x in vect : 
        if x == 0 : 
            z += 1 

            if z&1 :
                output.append('A') 
            else : 
                output.append('B')
        else :
            output.append('C')

    print("".join(output))

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
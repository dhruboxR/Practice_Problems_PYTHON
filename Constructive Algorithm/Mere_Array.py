# https://codeforces.com/problemset/problem/1401/C
import sys
import math 
input = sys.stdin.readline

"""
    LET'S TAKE GCD WITH THE MINIMUM ELEMENT AND MARK THAT POSITION  

    - i'th          :   4   3   6   6   2   9       here min element is 2 
    - gcd(ith, 2)   :  -1   3  -1  -1  -1   9       we have [ 4, 6, 6, 2 ] as swap options

    sort the swapOptions [4, 6, 6, 2] -> [ 2, 4, 6, 6 ] 
    Then whenever we find a -1 in the source we put value from options in order 
"""

def solve():
    n = int( input() )
    source = list( map(int, input().split()) )

    mn = min( source )  # minimum element of the source 

    options = []

    for i in range(n) : 
        if math.gcd(source[ i ], mn) == mn : 
            options.append( source[ i ] )
            source[ i ] = -1
    
    options.sort()  # sort the avaiable options
    idx = 0 

    for i in range(n) : 
        if source[ i ] == -1 : 
            source[ i ] = options[ idx ]
            idx += 1
    
    print( "yes" if source == sorted(source) else "no" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
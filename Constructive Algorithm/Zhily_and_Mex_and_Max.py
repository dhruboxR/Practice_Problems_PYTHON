# https://codeforces.com/contest/2224/problem/B

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    source.sort()

    # bring the unique elements in the front part 
    k = 0
    for i in range(length) :
        if k == 0 or source[ k-1 ] != source[ i ] :
            source[ k ] = source[ i ]
            k += 1

    mx = max( source )
    mtrack = score = 0
    
    if mx == 0 :
        print( length )
        return
    
    if length == 1 :
        print( max(1, mx) )
        return

    if length == 2 :
        if source[ 0 ] == 0 and source[ 1 ] == 1 :
            print(4)
        elif source[ 0 ] == 0 :
            print( mx*2 + 1 )
        else : print(mx * length)
        return
    
    inc = False
    score += mx

    for i in range(length-1) :
        score += mx 

        if source[ i ] == mtrack : mtrack += 1
        if mtrack == mx and not inc :
            mtrack += 1
            inc = True
        
        score += mtrack
        
    print( score )


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
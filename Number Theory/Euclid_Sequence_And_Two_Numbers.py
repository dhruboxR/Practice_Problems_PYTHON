# https://codeforces.com/problemset/problem/2234/A

import sys
input = sys.stdin.readline

def solve():
    length  = int( input() ) 
    source = list( map(int, input().split()) )

    source.sort( reverse = True )
    
    if length == 2 :
        print( *source )
        return
    
    for i in range(length-2) :
        if(source[ i ] % source[ i+1 ] != source[ i+2 ]) :
            print( -1 ) 
            return
    
    print( source[ 0 ], source[ 1 ] )


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
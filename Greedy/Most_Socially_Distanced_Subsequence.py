import sys
import math
input = sys.stdin.readline

"""
We take the first and the lastValue as the endpoints 
    For the values in between : 
        - a[ i-1 ] < a[ i ] > a[ i+1 ]   : peak 
        - a[ i-1 ] > a[ i ] < a[ i+1 ]   : bottom 

"""

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    finSequence = []                # list to store the final elements of the subSequence 

    for i in range(length) : 
        if i == 0 or i == length-1 : 
            finSequence.append( source[ i ] ) 
        elif source[ i ] > source[ i-1 ] and source[ i ] > source[ i+1 ] : 
            finSequence.append( source[ i ] ) 
        elif source[ i ] < source[ i-1 ] and source[ i ] < source[ i+1 ] : 
            finSequence.append( source[ i ] )
    
    print( len(finSequence) )
    print( *finSequence )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
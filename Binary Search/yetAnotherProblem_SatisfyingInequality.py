# https://codeforces.com/contest/1703/problem/F

from bisect import bisect_left

import sys
input = sys.stdin.readline

def solve():
    length = int( input()) 
    source = list( map(int, input().split()) )

    index = [] 
    key = []

    for idx in range(1, length+1) :
        value = source[ idx-1 ]     # converted to 0 based 

        if idx > value :
            index.append( idx )
            key.append( value )
    
    if not key :        # the lists are empty !!
        print( 0 )
        return

    pairCounter = 0
    # For each element from the back, how many earlier positions satisfy the condition involving key[ i ]
    for i in range( len(index)-1, -1, -1) :
        k = key[ i ]
        pairCounter += bisect_left(index, k)   # RETURNS : number of elements in list[index] that are < k
    
    print( pairCounter )
    

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()

#     bisect_left(index, k) returns:
#               number of elements in index that are < k

#     Because index is sorted increasing (it is by construction since idx increases).


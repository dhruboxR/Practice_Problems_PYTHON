# https://codeforces.com/contest/2242/problem/B

import sys
import math
input = sys.stdin.readline

"""
    In other words, you need to divide the array a into three pairwise disjoint contiguous non-empty parts so that, 
        - in the left part the number of ones is at least the total number of twos and threes, 
        - in the middle part the total number of ones and twos is at least the number of threes, 
        - and the right part can be anything, but it must be non-empty.

    /> The bug wasn't in the code — it was in reading the statement. 
    
    /> Got WN during contest -_- hurts right ?

    /> HAPPENS ! UPSOLVING FEELS GREAT THOUGH  :)
"""

def solve():
    n = int( input() )
    source = list( map(int, input().split()) )

    pos = []    # list to store the potential equalPoints 

    one = two = three = 0
    for i in range(n) : 
        if source[ i ] == 1 : one += 1
        elif source[ i ] == 2 : two += 1
        else : three += 1 

        if one >= two+three : 
            pos.append(i)
    
    for idx in pos : 
        a = b = c = 0
        for i in range(idx+1, n-1) : 
            if source[ i ] == 1 : a += 1
            elif source[ i ] == 2 : b += 1
            else : c += 1

            if a + b >= c : 
                print( "yes" )
                return
    
    print( "no" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
# https://codeforces.com/contest/2208/problem/A

import sys
input = sys.stdin.readline

def solve():
    n = int((input()))
    mxFreq = 0

    freq = {} # dictionary 

    for _ in range(n) :
        row = list(map( int,input().split()) )
        
        for value in row :
            freq[ value ] = freq.get( value, 0 ) + 1 
            mxFreq = max(mxFreq, freq[ value ])
    
    accumulate = n*n - mxFreq

    if accumulate < n : print( "no" ) 
    else : print( "yes" )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()


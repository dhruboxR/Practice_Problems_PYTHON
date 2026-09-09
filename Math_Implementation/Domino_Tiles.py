# https://codeforces.com/contest/2256/problem/B

import sys
import math
input = sys.stdin.readline

def flip(cherr) : 
    return '0' if cherr == '1' else '1'

def solve():
    n = int( input() )
    s = list( input().strip() )
    """
     STEP 1 & 2: SIMPLIFYING THE CONDITION & PARITY SEPARATION
     -------------------------------------------------------------
     The problem states that the weight of domino i (s[i] + s[i+1]) must 
        be different from the weight of domino i+1 (s[i+1] + s[i+2]).

     Mathematically: s[i] + s[i+1] != s[i+1] + s[i+2]  =>  s[i] != s[i+2]

     This splits the string into two completely independent parity groups:
       - Even positions: 0, 2, 4, 6...
       - Odd positions:  1, 3, 5, 7...
    """
    # Process even positions (0, 2, 4, 6,...)
    for i in range(0, n, 2) : 
        if s[ i ] == '?' : continue     # skip until we find a known character

        # fill the unknown characters going backwards 
        for j in range(i-2, -1, -2) :
            if s[ j ] == '?' : s[ j ] = flip( s[j+2] )
            elif s[ j ] == s[ j+2 ] : 
                print(0)
                return

        # fill the unknown characters going forwards 
        for j in range(i+2, n, 2) : 
            if s[ j ] == '?' : s[ j ] = flip( s[j-2] )
            elif s[ j ] == s[ j-2 ] : 
                print(0)
                return
        break

    # Process odd positions (1, 3, 5, 7,...) : same process as the evens 
    for i in range(1, n, 2) : 
        if s[ i ] == '?' : continue 

        for j in range(i-2, -1, -2) : 
            if s[ j ] == '?' : s[ j ] = flip( s[j+2] )
            elif s[ j ] == s[ j+2 ] : 
                print(0)
                return
        
        for j in range(i+2, n, 2) : 
            if s[ j ] == '?' : s[ j ] = flip( s[j-2] )
            elif s[ j ] == s[ j-2 ] : 
                print(0)
                return
        break

    """
     STEP 4: COUNTING THE WAYS
     -------------------------------------------------------------
     s[0] and s[1] independently determine the two independent parity groups.
    
     If s[0] is already known:
         only 1 possibility for the even positions group.
     If s[0] is still '?':
         it can be either 0 or 1 -> 2 possibilities.
    
     Same logic applies to s[1] for the odd positions group.

     Total ways = (choices for s[0]) * (choices for s[1])

     (Modulo 998244353 is naturally satisfied since the max answer here is at most 4).
    """
    ans = (2 if s[0] == '?' else 1) * (2 if s[1] == '?' else 1)
    print(ans)


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
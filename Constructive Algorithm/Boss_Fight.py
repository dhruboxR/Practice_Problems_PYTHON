# https://codeforces.com/problemset/problem/2252/A

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() ) 
    arr = list( map(int, input().split()) )
    freq = {}   # track the maximum frequency 

    mx = float('-inf')
    mxval = -1 

    for integer in arr : 
        freq[ integer ] = freq.get(integer, 0) + 1
        if freq[ integer ] > mx : 
            mxval = integer 
            mx = freq[ integer ]

    # frequence of other elements 
    others = n - mx 

    # mx <= others 
    if mx <= others : print( sum(arr) )
    else : 
        # mx > others 
        health = 0 
        for val, cnt in freq.items() : 
            if val != mxval : 
                health += val * cnt 

        health += others * mxval 
        freq[ mxval ] -= others 
        health += min(freq[ mxval ], 2) * mxval 
        
        print(health)
            

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

"""
    1. Count the frequency of every card value while keeping track of the value
    with the maximum frequency.

    2. Let:
        mx = maximum frequency
        mxval = value having the maximum frequency
        others = n - mx

    3. If mx <= others:
        We can rearrange the cards so that no two equal values are adjacent.
        Since the shield is never activated, every card deals damage.
        Answer = sum(arr).

    4. Otherwise (mx > others):
        - Use every non-maximum card to separate one occurrence of the most
            frequent value. This contributes:
                others * mxval
        - All other card values are always used, so add their total damage.
        - After pairing, only occurrences of mxval remain.
        - If one card remains, it can be played safely.
        - If two or more remain, only the first two can be played because the
            second consecutive occurrence activates the shield, preventing any
            further damage.
        - Therefore, the remaining contribution is:
                min(remaining_occurrences, 2) * mxval

    5. Output the total damage.
"""
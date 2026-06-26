# https://codeforces.com/contest/1504/problem/B

import sys
input = sys.stdin.readline

def solve():
    n = int( input() )
    a = input().strip()
    b = input().strip() 

    if a == b :
        print( "yes" )
        return
    if n == 1 :
        if a == b : print( "yes" )
        else : print( "no" )
        return
    
    # only where cnt0 == cnt1
    balance = matched = unmatched = 0
    idx = -1
    valid = True 

    # balanced point 
    """
        NOW FOR EACH PREFIX ,
        Either a[ i ] == b[ i ] for this prefix[ every idx ]
        Else   a[ i ] != b[ i ] for this prefix[ every idx ]
        can't have mixed value 
    """
    for i in range(n) :
        if a[ i ] == '0' : balance += 1
        else : balance -= 1

        if a[ i ] == b[ i ] : matched += 1
        else : unmatched += 1

        if balance == 0 :
            idx = i         # mark the last balanced index 

            # Mixed Block -> impossible 
            if matched > 0 and unmatched > 0 : 
                valid = False
                break

            matched = 0
            unmatched = 0
        
    # final check : after the balanced index each a[ i ] == b[ i ] must hold 
    if valid : 
        for i in range(idx+1, n) : 
            if a[ i ] != b[ i ] : 
                valid = False 
                break
    
    print( "yes" if valid else "no" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
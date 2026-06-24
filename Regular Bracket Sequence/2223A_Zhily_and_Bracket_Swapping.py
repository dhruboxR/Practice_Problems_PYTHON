# https://codeforces.com/problemset/problem/2223/A

import sys
input = sys.stdin.readline

def is_valid(sequence) :
    balance = 0

    for ch in sequence :
        if ch == '(' : balance += 1
        else : balance -= 1

        # ')' came before '('
        if balance < 0 : 
            return False 
    
    # Balance must be zero for a Regular Bracket Sequence at the end 
    return balance == 0

def solve():
    n = int( input() )
    a = list( input().strip() )
    b = list( input().strip() )

    """
    NUMBER OF POSITIONS WHERE a[i] != b[i]

    For such positions:
    odd flexible positions  -> '('
    even flexible positions -> ')'
    """
    counter = 0
    for i in range(n) :
        # Fixed position, swapping does nothing 
        if a[ i ] == b[ i ] :
            continue

        counter += 1 

        if counter&1 :
            a[ i ] = '('
            b[ i ] = ')'
        else :
            a[ i ] = ')'
            b[ i ] = '('
    
    # Finally check if both strings are Regular Bracket Sequences
    if is_valid(a) and is_valid(b) :
        print( "yes" ) 
    else : 
        print( "no" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
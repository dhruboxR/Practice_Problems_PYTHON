# https://codeforces.com/contest/2222/problem/B

import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split()) 

    odd = []
    even = []

    source = list( map(int, input().split()) )
    
    # odd index values || even index values 
    for i in range(n) :
        if (i+1)&1 : odd.append( source[ i ] )
        else : even.append( source[ i ] )
    
    # sorting the lists 
    odd.sort()
    even.sort()

    odd_flag = False
    even_flag = False


    ids = list( map(int, input().split()) )

    for idx in ids :
            #   odd positions & even positions
            #   best remaining value is negative
            #   AND we've already marked one this parity element before
        if idx&1 :      
            if odd and not( odd[-1] < 0 and odd_flag ) :
                odd.pop()
                odd_flag = True
        else :
            if even and not( even[-1] < 0 and even_flag ) :
                even.pop()
                even_flag = True
    
    remaining_sum = sum(odd) + sum(even)        # remaining unmarked elements 
    print( remaining_sum )


testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
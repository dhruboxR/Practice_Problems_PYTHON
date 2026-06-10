# https://codeforces.com/contest/2233/problem/B

import sys
input = sys.stdin.readline

def solve():
    length = int( input() )
    s = length * 4

    if length <= 3 :
        if length == 2 :
            print("1 2 1 1 2 2 1 2")
        else :
            print("1 1 2 1 2 3 1 3 2 2 3 3")
        return
    
    source = [0] * s
    curr = 1
    for i in range(0, 2*length, 2) :
        source[ i ] = curr 
        source[ i+1 ] = curr
        
        curr += 1
    
    temp = [i+1 for i in range(length)]
    
    # rotate left by 1 
    temp = temp[1:] + temp[:1]
    idx = 0 
    for i in range(2*length, 3*length) :
        source[ i ] = temp[ idx ]
        idx += 1
    
    # rotate left by 2 
    temp = temp[2:] + temp[:2]
    idx = 0
    for i in range(3*length, 4*length) :
        source[ i ] = temp[ idx ]
        idx += 1

    print( *source )


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
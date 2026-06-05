# https://codeforces.com/contest/1635/problem/C
import sys
input = sys.stdin.readline

def solve():
    length = int( input() )
    src = list( map(int, input().split()) )

    # initially sorted 
    if src == sorted(src) : 
        print( 0 ) 
        return
    if src[ -1 ] < src[ -2 ] :
        print( -1 ) 
        return
    
    # only possible if the last element is positive 
    if src[ -1 ] < 0 :
        print( -1 )
        return
    
    op = []
    dif = src[ -2 ] - src[ -1 ]

    for i in range(0, length-2) :
        if src[ i ] > dif or src[ i ] < src[ i-1 ] :
            src[ i ] = dif
            op.append(i+1)

    print( len(op) )
    for val in op :
        print(val, length-1, length)




testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
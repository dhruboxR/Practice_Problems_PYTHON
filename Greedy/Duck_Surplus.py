# https://codeforces.com/problemset/problem/2237/C
import sys
input = sys.stdin.readline

def solve():
    n = int( input() )
    src = list( map(int, input().split()) )
    
    if n == 1 :
        print( src[ 0 ] )
        return
    
    # check consecutive elements 
    for i in range(n-1) :
        if src[ i ] > src[ i+1 ] :
            src[ i+1 ] += src[ i ]
    
    # check the last 
    if src[ n-1 ] < src[ n-2 ] : print(src[n-1] + src[n-2])
    else : print( src[ n-1 ] )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
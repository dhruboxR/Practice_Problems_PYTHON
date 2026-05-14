# https://codeforces.com/contest/2209/problem/B
import sys
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    for i in range(length) :
        greater = smaller = 0

        for j in range(i+1, length) :
            if source[ i ] > source[ j ] : 
                smaller += 1
            elif source[ i ] < source[ j ] : 
                greater += 1
        print( max(smaller, greater), end = ' ' )
    print( '\n' )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
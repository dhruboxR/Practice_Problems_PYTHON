import sys
import math
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split()) 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < 2*m :
        print("no")
        return 

    # we can compare the endpoints that's all 
    a.sort()
    b.sort()

    for i in range(m) : 
        if a[ i ] > b[ i ] :
            print("no")
            return 

    # iterate in reverse 
    j = n-1 
    for i in range(m-1, -1, -1) : 
        if a[ j ] < b[ i ] : 
            print("no")
            return 
        j -= 1

    print( "yes" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
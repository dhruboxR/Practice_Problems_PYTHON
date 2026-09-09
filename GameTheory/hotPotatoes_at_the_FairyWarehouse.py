# https://codeforces.com/problemset/problem/2255/A

import sys
import math
input = sys.stdin.readline

# optimal is to hold the potatoes till the last round and then perform the valid transfers 
# so basically the games lasts for only 1 round 

def solve():
    n, k = map(int, input().split()) 
    string = list( input().strip() )

    n *= 2 
    temp = string.copy() 
    
    for i in range(n) : 
        if i+1 < n : 
            if string[ i ] == '1' and string[ i+1 ] == '0' : 
                temp[ i ] = '0'
                temp[ i+1 ] = '1'
        else : 
            if string[ i ] == '1' and string[ 0 ] == '0' : 
                temp[ i ] = '0'
                temp[ 0 ] = '1'

    oddRed = evenBlue = 0 
    for i in range(n) : 
        oddRed += ( 1 if ((i&1) and temp[ i ] == '1') else 0 )
        evenBlue += ( 1 if ((i%2 == 0) and temp[ i ] == '1') else 0 )

    print(oddRed, evenBlue)

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
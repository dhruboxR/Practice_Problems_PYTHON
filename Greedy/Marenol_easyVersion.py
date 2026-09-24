# https://codeforces.com/problemset/problem/2254/C1

import sys
import math
input = sys.stdin.readline

# The operation can be treated as swapping ai with ai+2

def solve():
    n = int( input() ) 
    a = input().strip() 
    b = input().strip()

    # The number of 1's in string a must be equal to the number of 1's in string b 
    for i in range(2) : 
        cntA = cntB = 0

        for j in range(i, n, 2) :
            if a[j] == '1' : cntA += 1
            if b[j] == '1' : cntB += 1

        if cntA != cntB : 
            print("no")
            return 

    print( "yes" ) 


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
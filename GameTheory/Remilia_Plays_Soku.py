# https://codeforces.com/problemset/problem/2228/B

import sys
input = sys.stdin.readline

def solve():
    len, x1, x2, k = map(int, input().split())

    # if the length of the circular path is less than 4 then it's always 1    
    if len < 4 :
        print(1) 
        return
    
    # the circular path has two ways 1. clockWise run 2. anti clockWise run
    # the chaser took the minimum distance to chase 
    # the runner can atmost survive min(abs(x1 - x2), len - abs(x1 - x2)) + k

    print( min(abs(x1-x2), len-abs(x1-x2)) + k )
    

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
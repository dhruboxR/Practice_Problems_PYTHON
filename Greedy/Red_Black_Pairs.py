# https://codeforces.com/contest/2225/problem/C

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

# Greedy : if a vertical cell is pair we take it first 
# vertical pair consumes 2 cells , horizontal pair consumes 4 cells
# we only choose horizontal pair when we have atleast 1 horizntal pair among 2 rows

def solve():
    length = int( input() )
    r1 = input().strip()
    r2 = input().strip()

    opCounter = i = 0
    while i < length :
        if r1[ i ] == r2[ i ] :         # vertical pair
            i += 1
            continue    

        if i+1 < length and (r1[ i ] == r1[ i+1 ] or r2[ i ] == r2[ i+1 ]) :
            opCounter += (r1[ i ] != r1[ i+1 ]) 
            opCounter += (r2[ i ] != r2[ i+1 ])
            i += 2
        else :
            opCounter += 1
            i += 1
    
    print( opCounter )
    

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
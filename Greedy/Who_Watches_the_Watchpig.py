# https://codeforces.com/problemset/problem/2245/A
import sys
import math
input = sys.stdin.readline

"""
If a piggy faces left (L), any watchpig pair it belongs to must involve a piggy to its left facing right (R). 
Symmetric logic applies if it faces right.

Consider a piggy at index i (1 ≤ i ≤ k). It cannot face L because,
there are at most (i-1 < k) piggies to its left, meaning it cannot form k watchpig pairs. 
    - Thus, the leftmost k piggies must all face R
    - By the same reasoning, the rightmost kpiggies must all face L

Therefore, if 2k>n, the prefix and suffix overlap, and there is no solution. 

"""

def solve():
    n, k = map(int, input().split())
    string = input().strip()

    if 2*k > n : 
        print( -1 )
        return

    # leftmost k piggies R
    mov = 0 
    for i in range(k) : 
        if string[ i ] == 'L' : mov += 1
    for i in range(n-1, n-k-1, -1) : 
        if string[ i ] == 'R' : mov += 1

    print(mov)  

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
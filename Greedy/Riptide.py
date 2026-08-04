# https://codeforces.com/contest/2254/problem/A

import sys
import math
input = sys.stdin.readline

def solve():
    n = 3
    arr = list(map(int, input().split()))

    arr.sort()
    if arr[ 0 ] == arr[ 1 ] or arr[ 1 ] == arr[ 2 ] :
        print(0)
        return

    move = 0
    found = False 

    while not found : 
        arr[ 0 ] += 1
        arr[ 2 ] -= 1
        move += 1

        arr.sort()
        if arr[ 0 ] == arr[ 1 ] or arr[ 1 ] == arr[ 2 ] : 
           found = True 

    print( move )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
# https://codeforces.com/problemset/problem/1359/B

import sys
import math
input = sys.stdin.readline

# two pointer + greedy approach

def solve():
    n, m, x, y = map(int, input().split())
    cost = 0

    for i in range(n) : 
        string = input().strip()

        l = 0
        while l < m : 
            if string[l] == '*' : 
                l += 1 
                continue 

            r = l 
            while r+1 < m and string[r+1] == '.' : r += 1 

            sz = r - l + 1 

            if 2*x <= y : cost += sz * x 
            else : cost += ((sz//2)*y + (sz%2)*x) 

            l = r + 1

    print(cost) 


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

    
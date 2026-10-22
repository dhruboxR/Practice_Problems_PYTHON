# https://codeforces.com/problemset/problem/2261/C

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    src = list(map(int, input().split())) 

    sum = odd = even = 0 

    for x in src : 
        sum += x 
        if x&1 : odd += 1 
        else : even += 1 

    if n == 1 or sum % 2 == 0 : 
        print("moggity") 
    elif odd and not even : 
        print("moggity" if n != 3 else "larpity") 
    else :
        # odd-even both & the sum is not even 
        print("larpity" if n == 2 else "moggity")

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
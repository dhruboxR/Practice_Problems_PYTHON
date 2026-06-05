# https://codeforces.com/contest/1671/problem/C

import sys
input = sys.stdin.readline

def solve():
    length, cash = map(int, input().split())
    price = list(map(int, input().split()))

    price.sort()
    
    prefix = [0] * length
    for i in range(length) :
        if i == 0 : prefix[ i ] = price[ i ]
        else : prefix[ i ] = prefix[ i-1 ] + price[ i ]
    
    sugarcane = 0

    for i in range(length) :
        low, high, best = 1, 10**9, 0

        # for how many days this packet can be bought with the cash 
        while low <= high :
            mid = (low + high) // 2
            cost = prefix[ i ] + (i+1) * (mid -1)

            if cost <= cash :
                best = mid
                low = mid + 1
            else :
                high = mid - 1
        
        sugarcane += best
    
    print( sugarcane )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
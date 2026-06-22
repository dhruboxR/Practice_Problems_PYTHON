# https://codeforces.com/problemset/problem/2208/B
import sys
input = sys.stdin.readline

def solve():
    n, k, p, m = map(int, input().split())
    p -= 1
    k -= 1
    
    src = list(map(int, input().split()))
    ans = total = 0
    dist = p
    ace = src[ p ]

    # Till energy burns out 
    while total <= m :
        if dist <= k :
            total += ace 
            if total <= m : ans += 1

            # copy the original source 
            reorder = src[:]
            reorder.append(ace)     # put the Ace at the back 
            reorder.pop(dist)       # remove the used Ace 

            src = reorder 
            dist = n-1 

        else :
            # choose the minimum element from the removable cards 
            mn = float('inf')
            idx = 0 

            for i in range(k+1) :
                if src[ i ] < mn :
                    mn = src[ i ] 
                    idx = i
            
            total += mn     # remove the minimum element 
            
            reorder = src[:]
            reorder.append(mn)
            reorder.pop(idx)

            src = reorder 
            dist -= 1   # Ace move closer

    print( ans )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
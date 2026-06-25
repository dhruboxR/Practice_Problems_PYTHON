# https://codeforces.com/problemset/problem/1470/A

import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split() )
    
    # k[ i ] : maximum gift friend i can recieve
    k = list( map(int, input().split()) )

    # c[ i ] : cost of the gift
    c = list( map(int, input().split()) )

    # Friends with larger k have more expensive default costs.
    # Process them first so they get the cheapest available gifts.
    k.sort( reverse = True )

    totalCost = ptr = 0

    for i in range(n) : 
        """
        Can we give the cheapest unused gift ? 
        ptr < k[ i ] and c[ ptr ] < c[ k[i]-1 ]
        """
        if ptr < k[ i ] and c[ ptr ] < c[ k[i]-1 ] :
            # Provide the gift, add the cost, move the ptr 
            totalCost += c[ ptr ]
            ptr += 1
        else :
            # Giev money instead 
            totalCost += c[ k[i]-1 ]
    
    print( totalCost )
    

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
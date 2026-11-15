# https://codeforces.com/problemset/problem/2278/C

import sys
import math
input = sys.stdin.readline

"""
    2 1 1 1 2   middle elements all 1 -> totalSum - s[0] - s[n-1] == n-2
        # Answer : totalSum - (n-2) - 1  
    
    1 1 2 1  element > 1 exists in the middle 
    1 2 2 
    2 3 
    4 
        # Answer : totalSum - 1 
"""

def solve():
    n = int(input())
    src = list(map(int, input().split())) 
    """
        Any element from 2 till n-1 must be > 1 for traversing with minimum value loss 
                -> choose that element and expand outwards  

        if edge elements is > 1 then we have to choose that : value loss = (number of steps moved) 
    """
    totalSum = sum( src ) 

    if totalSum == n :      # all elements are 1  
        print(-1) 
        return 

    # check if all the middle elements are 1 
    if totalSum - src[0] - src[-1] == n - 2 : 
        # edge case if n == 2
        if n == 2 : print(totalSum - 1)
        else : print(totalSum - (n-2) - 1)
    else : 
        print(totalSum - 1) 
    

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
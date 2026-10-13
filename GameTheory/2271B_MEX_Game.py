# https://codeforces.com/contest/2271/problem/B

import sys
import math
input = sys.stdin.readline

"""
    # If a card's frequency is >= 2*k then 
        - Each player will surely get at least k of them [ leave them ]
    
    # Now for the card which appears 2*k-1 times 

            8 2 
            1 1 1 0 0 0 0 0

        alice : 1 1 0 0  : mex is 2  
        bob   : 1 0 0 0  : mex is 1
            
    ### SO, ALICE WINS IF AND ONLY IF 
            - there is number with frequency == (2*k-1) present in the array 
----------------------------------------------------------------------------------------

    ### But if there is any card with frequency < 2*k - 1
        - Then this will be the MEX no matter how they play the game 
"""

def solve() :
    n, k = map(int, input().split())
    src = list( map(int, input().split()) ) 
    
    freq = [0] * (n+1)  # listt to count the frequencies from 0 to n 
    for value in src : freq[value] += 1  

    for val in range(n+1) : 
        if freq[val] < 2*k : 
            if freq[val] == 2*k - 1 : 
                print("yes")
            else : 
                # this is the bottleneck : the MEX will be this value no matter what 
                print("no") 
            return 
        
testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
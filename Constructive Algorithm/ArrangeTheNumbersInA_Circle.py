# https://codeforces.com/problemset/problem/2230/C

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )
    
    canTake = current = 0
    multiple = valid = False

    for value in source :
        if value > 1 :
            valid = True
            if current > 0 : multiple = True
            
            current += value       
            canTake += ( value // 2 ) - 1
    
    extra = sum(source) - current
    if not multiple : canTake += 1

    # we have to have enough spare values to fit inside
    finLen = current + min(canTake, extra)     

    if not valid or finLen < 3 : print( 0 )     # minimum length of 3 is required
    else : print( finLen )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

# got a way out now, during contest wasn't able to find a way out --- BRAIN WAS NOT BRAINING THEN -_-
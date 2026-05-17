# https://codeforces.com/contest/2228/problem/A

import sys
input = sys.stdin.readline

def solve():
    bound = int( input() )
    source = list( map(int, input().split()) )

    one = two = moveCounter = 0
    for value in source :
        if value == 1 : one += 1
        elif value == 2 : two += 1
        else : moveCounter += 1
    
    inf = min(one, two)
    one -= inf
    two -= inf
    print(moveCounter + inf + (one//3) + (two//3))

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
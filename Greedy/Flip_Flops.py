# https://codeforces.com/contest/2209/problem/A

import sys
input = sys.stdin.readline

def solve():
    n, combat, ff = map(int, input().split())
    hp = list( map(int, input().split()) )

    hp.sort()
    for health in hp :
        if combat < health : 
            print( combat )
            return
        
        add = combat - health
        combat += health

        if ff >= add :
            combat += add
            ff -= add 
        else :
            combat += max(0, ff)
            ff -= max(0, ff)
    
    print( combat )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
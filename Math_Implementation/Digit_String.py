# https://codeforces.com/contest/2230/problem/B

# every single 4 counts
# 1...2 || 3...2 also counts

import sys
input = sys.stdin.readline

def solve():
    string = input().strip()
    one = two = three = moveCounter = 0

    for character in string :
        if character == '1' : one += 1
        elif character == '3' : three += 1
        elif character == '4' : moveCounter += 1
        else :
            # 2 appears
            if one > 0 :
                one -= 1
                moveCounter += 1
            elif three > 0 :
                three -= 1
                moveCounter += 1
    
    print( moveCounter )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
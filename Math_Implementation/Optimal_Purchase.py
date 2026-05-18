# https://codeforces.com/contest/2230/problem/A

# Individual key: costs a dollars and gives access to one student.
# Group key: costs b dollars and gives access to a group of up to 3 students inclusive.

import sys
input = sys.stdin.readline

def solve():
    students, individualCost, groupCost = map(int, input().split())

    # if 3*individualCost > groupCost - optimal is to use the group cost
    if 3*individualCost > groupCost :
        moneyNeeded = (students // 3) * groupCost
        
        if students % 3 :
            # some students still remains
            remIndcost = (students % 3) * individualCost
            moneyNeeded += min(groupCost, remIndcost)

        print( moneyNeeded )
    else : 
        print(individualCost * students)
    

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()



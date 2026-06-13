# https://codeforces.com/problemset/problem/2236/C

import sys
input = sys.stdin.readline

def solve():
    a, b, x = map(int, input().split())
    
    if a == b :
        print(0)
        return
    
    div = 0
    ans = 10**18

    while a != b :
        ans = min(ans, div + abs(a-b))

        if a > b : a //= x
        else : b //= x

        div += 1

    ans = min(ans, div)  # final state a == b so div+abs(a-b) where, abs(a-b)= 0
    print( ans )


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()


# If a > b, dividing b can never help because it only makes the difference larger:
#   So every useful division should be applied to the larger number.

# At any state, we have two choices:
#       Stop dividing and make the numbers equal using only +1 operations → cost = |a-b|.
#       Divide the larger number once more → cost increases by 1.

# Therefore, while repeatedly dividing the larger number, keep track of:
#                   divisions used+∣a−b∣

# The minimum value over all states (including when a == b) is the answer. 

# Complexity: O(log(max(a,b))).
# https://codeforces.com/problemset/problem/1366/B

import sys
input = sys.stdin.readline

def solve():
    n, x, m = map(int, input().split())

    # current segment which contains 1
    l = r = x
    for i in range(m) :
        left_bound, right_bound = map(int, input().split())

        # No Intersection 
        if left_bound > r or right_bound < l : continue 
        else :
            # INTERSECTION 
            l = min(l, left_bound)
            r = max(r, right_bound)

    print( r - l + 1 ) 

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

"""
        Initially, the position of 1 is fixed at x, so the reachable range is [x, x].
        
        For every interval [l, r]:
            - If it overlaps with the current reachable range,
              expand the reachable range by taking their union.
              
            - Otherwise, ignore it since 1 cannot reach that interval.

        After processing all intervals,
        every position inside the final reachable range can contain 1.

        Answer = length of the reachable range = R - L + 1.
"""
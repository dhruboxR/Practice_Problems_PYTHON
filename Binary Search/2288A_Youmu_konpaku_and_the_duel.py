# https://codeforces.com/problemset/problem/2288/A

import sys
import math
input = sys.stdin.readline
"""
Problem Overview:
    Youmu starts with attack power 1 and 0 stacks. In each move, she can either:

    1. Charge: gain 1 stack and increase attack power by 1.

    2. Attack: deal damage equal to her current attack power, then decrease stacks by 1
    (if she has any). Attack power drops by 1 when a stack is consumed, down to a
    minimum of 1 once stacks reach 0.

We want the minimum total moves to deal at least `health` damage.

Key Idea & Optimization:

    - Charging first and attacking later never hurts total damage for a fixed number of
    charges `c` and attacks `mov`.

    - After `c` charges, Youmu's initial attack power is `1 + c` with `c` stacks. Each
    attack deals the current attack power and reduces stacks (and attack power) by 1
    while stacks > 0; once stacks hit 0, subsequent attacks deal 1 damage each.

    - Attacking `health` times with 0 charges takes `health` moves, giving a valid
    initial upper bound `ans = health`.

    - For each charge count `c < ans`, the total damage from `mov` attacks is non-decreasing
    in `mov`, so we binary search `mov` in `[1, ans]` for the smallest attack count
    that achieves `damage >= health`. If found, we update `ans = min(ans, c + mov)`.

    - Bounding `c < ans` and `high = ans` keeps the search space small (around ~244
    for health <= 10,000), avoiding TLE.
"""

# THIS PYTHON IMPLEMENTATOIN GETS ' TLE ' BY THE WAY !! -_-

def calc_damage(c: int, mov: int) -> int : 
    damage = 0
    attack = 1 + c
    stacks = c 

    for _ in range(mov) : 
        damage += attack 
        if stacks > 0 : 
            stacks -= 1 
            attack -= 1

    return damage

def solve():
    health = int( input() )
    ans = health;   # Attacking 'health' times with 0 charges always works 

    # traverse the charge level and mod the moves required 
    for c in range(ans) : 
        low = 1
        high = health 

        while low <= high : 
            mid = low + (high - low) // 2 

            if calc_damage(c, mid) >= health : 
                if c + mid < ans : 
                    ans = c + mid 
                high = mid - 1
            else : 
                low = mid + 1 

    print(ans) 

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
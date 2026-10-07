import sys
import math
input = sys.stdin.readline

"""
        - Test all split points where the string transitions from 0's to 1's 
        - A split after index k means the first k elements must be '0' and the remaining must be '1'

        - turn ones on the left into zeros (count of 1's till now)
        - turn zeros on the right into ones (zero's on the right)
"""

def solve():
    n = int( input() )
    s = input() 

    cZero = s.count('0')
    if s[0] == '1' : 
        print(cZero) 
        return 

    oneOnLeft = 0 
    move = float('inf')

    for i in range(n) : 
        if s[i] == '1' : oneOnLeft += 1

        zero_on_right = cZero - (i+1 - oneOnLeft)
        move = min(move, oneOnLeft + zero_on_right)

    print(move)


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
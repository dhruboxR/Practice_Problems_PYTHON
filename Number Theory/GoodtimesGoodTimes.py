# https://codeforces.com/problemset/problem/2241/B
import sys
input = sys.stdin.readline

"""
integer is good if it contains only 2 distinct digits 
x - already good 
y - choose y such that it is good and the mulRes of x * y is also good 
REPEAT , X | X 
4 * 11 = 44 
73 * 101 = 7373
299 * 1001 = 299299
6767 * 100001 = 67676767
"""

def solve():
    value = input().strip() 
    s = len( value ) 
    
    print((10**s) + 1)


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
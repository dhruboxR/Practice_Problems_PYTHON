# https://codeforces.com/contest/2233/problem/A
import sys
input = sys.stdin.readline

def solve():
    n, x, y, z = map(int, input().split()) 

    # time required without using AI 
    t1 = (n + x + y - 1) // (x+y)

    # time required using AI
    t2 = z
    remaining = n - (x*z)

    t2 += (remaining + (x + (10*y)) - 1) // (x+ 10 * y)

    print( min(t1, t2))

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
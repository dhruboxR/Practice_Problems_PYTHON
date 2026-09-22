# https://codeforces.com/problemset/problem/2260/B

import sys
import math
input = sys.stdin.readline

def solve():
    employee, project, time = map(int, input().split()) 
    diff = project - employee

    work_done = 0

    while time : 
        time -= 1
        
        work_done += (project % employee) 

        if project % employee == diff : break

        employee += 1 
        project += 1 

    work_done += (diff * time)
    print( work_done )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
# https://codeforces.com/contest/2261/problem/A

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() ) 
    string = input() 

    ones = string.count('1') 

    if ones <= 2 : 
        if ones == 1 : print(0)
        else : print(1)         # after one exchange operation answer = 1
    else : 
        for i in range(n) : 
            if string[i] == '1' : 
                for j in range(n-1, -1, -1) : 
                    if string[j] == '1' : 
                        print(abs(i - j))
                        return 

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
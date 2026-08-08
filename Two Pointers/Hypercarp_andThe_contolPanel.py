# https://codeforces.com/contest/2253/problem/B
import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    arr = list( map(int, input().split()) )

    # initially count the number of blocks that are currently present 
    blocks = 1
    for i in range(n) : 
        if i > 0 : 
            if arr[ i-1 ] != arr[ i ] : 
                blocks += 1

    # at max the answer can be blocks+2, blocks+1 is also possible 
    one = two = False 
    for i in range(n) :
        if i+3 < n : 
            if arr[i] == arr[i+1] and arr[i+2] == arr[i+3] and arr[i+1] != arr[i+2] : 
                two = True 
            if arr[i] == arr[i+1] and arr[i+1] != arr[i+2] and arr[i+1] != arr[i+3] :
                one = True 
        if i >= 3 : 
            if arr[i] == arr[i-1] and arr[i-1] != arr[i-2] and arr[i-1] != arr[i-3] : 
                one = True 

    # well, the front and the back check for one 1 2 2 ..... 1 1 2 
    if n >= 3 : 
            if arr[0] != arr[1] and arr[1] == arr[2] : 
                one = True 
            if arr[n-1] != arr[n-2] and arr[n-2] == arr[n-3] : 
                one = True 

    if two : print(blocks+2) 
    elif one : print(blocks+1) 
    else : print(blocks) 
                        

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
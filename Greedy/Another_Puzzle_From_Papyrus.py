# https://codeforces.com/contest/2238/problem/A
import sys
input = sys.stdin.readline

def solve():
    n, t = map(int, input().split()) 

    a = list( map(int, input().split()) )
    b = list( map(int, input().split()) )

    if a == b :         # DON'T FORGET ABOUT THE EDGE !!
        print( 0 )
        return

    # if can be done without reordering the elements 
    time = 0
    for i in range(n) : 
        if a[ i ] >= b[ i ] : time += a[ i ] - b[ i ]
        else :
            time = 0
            break

    a.sort()
    b.sort()

    curr = t
    for i in range(n) : 
        if a[ i ] < b[ i ] : 
            if time == 0 : 
                print( "-1" )
                return
            else : break
        else : 
            curr += a[ i ] - b[ i ]
    
    if time != 0 : 
        print( min(time, curr) ) 
    else : print( curr ) 


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
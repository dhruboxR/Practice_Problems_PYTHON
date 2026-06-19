# https://codeforces.com/problemset/problem/2237/B

import sys
input = sys.stdin.readline

def solve():
    length = int( input() )

    a = list( map(int, input().split()) )
    b = list( map(int, input().split()) )

    # bringing the first element less than or equal to this 
    cnt_second = 0
    for i in range(length) :
        idx = -1 
        j = i
        for j in range(i, length) :     # from current to right -> i till n
            if a[ j ] <= b[ i ] :       # a[j] gets mapped with b[i] 
                idx = j
                break
        
        if idx == -1 :
            print( "-1" ) 
            return
        
        # else we need to swap the segment for upcoming calculations
        for j in range(idx, i, -1) :
            # swap with the earlier element 
            a[ j ], a[ j-1 ] = a[ j -1 ], a[ j ]
            cnt_second += 1
    
    print( cnt_second )
    

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
# https://codeforces.com/contest/2254/problem/D

# SAME SOLUTION IN C++ GOT AC, BUT TLE IN PYTHON :)

import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    shadow = list(map(int, input().split()))

    sval = []   # store the distinct shadow values 
    freq = {}   # store the frequencies for the shadows 

    for val in shadow : 
        if val not in freq : 
            sval.append( val ) 
            freq[ val ] = 0
        freq[ val ] += 1

    sval.sort()    # sort the distinct shadow values 

    # if no 0, then invalid 
    if 0 not in freq : 
        print(-1)
        return 

    # if there is only one distinct shadow 
    if len(sval) == 1 : 
        print(*([1]*n))
        return 

    # recover the original values and map to corresponding shadow 
    ans = {}

    for i in range( len(sval) ) : 
        # the last value 
        if i == len(sval) - 1 : ans[ sval[i] ] = ans[ sval[i-1] ] + 1
        else : 
            diff = sval[i+1] - sval[i] 

            # original answer values must be whole integer 
            if diff % freq[ sval[i] ] != 0 : 
                print(-1) 
                return 

            ans[ sval[i] ] = diff // freq[ sval[i] ] 

            # original values must be strictly increasing 
            if i > 0 and ans[ sval[i] ] <= ans[ sval[i-1] ] :
                print(-1)
                return 

    # print the answer values 
    result = [str(ans[x]) for x in shadow]
    sys.stdout.write(" ".join(result) + "\n")

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
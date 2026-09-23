# https://codeforces.com/contest/2252/problem/B
import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    s = input().strip()

    delZero = delOne = 0
    # count how many 1's and 0's needed to be deleted to make the string alternating 
    for i in range(1, n) : 
        if s[ i ] == s[ i-1 ] :
            if s[ i ] == '0' : delZero += 1
            else : delOne += 1

    move = delZero + delOne 

    if abs(delZero - delOne) <= 1 :     # already satisfies the condition  
        print( move )
        return

    """
    Else we need to delete some additional characters that was deleted less. 
    The additional deletion can only be made from the two endpoints 
    """
    if delZero > delOne : 
        delExtra = abs(delZero - delOne) - 1
        available = (s[0] == '1') + (s[n-1] == '1')

        if available >= delExtra :
            print( move + delExtra )
            return 
        else :
            print( -1 )
    else : 
        delExtra = abs(delZero - delOne) - 1
        available = (s[0] == '0') + (s[n-1] == '0')

        if available >= delExtra : 
            print( move + delExtra )
            return 
        else : 
            print( -1 )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
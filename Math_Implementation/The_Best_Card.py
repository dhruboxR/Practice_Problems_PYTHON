import sys
import math
input = sys.stdin.readline

def solve():
    length = int( input() )
    length += 1

    # we just need to check if the new length is prime ! 
    i = 2; 
    while i*i <= length : 
        if length % i == 0 : 
            print( "no" )
            return
        i += 1
        
    print( "yes" )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
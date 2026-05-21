# https://codeforces.com/contest/1669/problem/E

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

#      Iterate through all given strings 
#      Generate all strings that differ in exactly one position, 
#      Count the number of times these strings occur in the array.

def solve():
    length = int( input() )
    occurance = {}          # dictionary to keep track of frequency

    letterBox = "abcdefghijk"
    totalPair = 0

    for _ in range( length ) :
        current = input().strip()
        occurance[ current ] = occurance.get(current, 0) + 1

        # change the first Character [ from 'a' till 'k' ]
        for cherr in letterBox :
            if current[ 0 ] == cherr : continue

            temp = cherr + current[ 1 ]
            totalPair += occurance.get(temp, 0)
        
        # change the second Character [ from 'a' till 'k' ]
        for cherr in letterBox : 
            if current[ 1 ] == cherr : continue

            temp = current[ 0 ] + cherr
            totalPair += occurance.get(temp, 0)
    
    print( totalPair )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
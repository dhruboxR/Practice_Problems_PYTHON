import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def zeroBorderedPalindrome(source, length, p1, p2, mex) :
    temp = set()

    # if expandable outside borders
    while p1 > 0 and p2 < length-1 and source[ p1-1 ] == source[ p2+1 ] :
        p1 -= 1
        p2 += 1
    
    while p1 < p2 :
        if source[ p1 ] == source[ p2 ] :
            temp.add( source[ p1 ])
            p1 += 1
            p2 -= 1
        else :
            return 1      # not a palindrome
        
    if p1 == p2 : temp.add( source[ p1 ] )

    for i in range(0, length+1) :
        if i not in temp : 
            return max(mex, i)

def zeroCenteredPalindrome(source, length, pos, mex) :
    temp = set()
    temp.add(0)

    if pos == 0 or pos == length-1 : return 1   # not valid for surrounded palindrome

    l = pos-1
    r = pos+1

    while l >= 0 and r < length and source[ l ] == source[ r ] :
        temp.add( source[ l ] )
        l -= 1
        r += 1

    for i in range(0, length+1) :
        if i not in temp :
            return max(mex, i )

def solve():
    length = int( input() )
    length *= 2

    source = list( map(int, input().split()) )

    z1 = z2 = -1        # mark the position of the 0's        
    for i in range(length) :
        if source[ i ] == 0 :
            if z1 == -1 : z1 = i
            z2 = i

    mex = 1     # we can always have the maximum mex as 1

    # 0 is the bordered elements and may or may not be expandable
    mex = max(mex, zeroBorderedPalindrome(source, length, z1, z2, mex))

    # 0 is the centered element and the palindrome is surrounded 
    mex = max(mex, zeroCenteredPalindrome(source, length, z1, mex))
    mex = max(mex, zeroCenteredPalindrome(source, length, z2, mex))

    print( mex )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
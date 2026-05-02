# https://codeforces.com/contest/2227/problem/C

import sys
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    both, none, two, three = [], [], [], []

    for value in source :
        if value % 2 == 0 and value % 3 == 0 :
            both.append( value )

        elif value % 2 != 0 and value % 3 != 0 :
            none.append( value )

        elif value % 2 == 0 and value % 3 != 0 :
            two.append( value )

        else : three.append( value )
    
    # both + two + none + three
    print( *(both + two + none + three) )


testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()
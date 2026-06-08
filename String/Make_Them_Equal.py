# https://codeforces.com/contest/1594/problem/C

import sys
input = sys.stdin.readline

def solve():
    length, cherr = input().split()
    length = int( length )

    string = input().strip()

    # initially all characters are equal to cherr
    if all(character == cherr for character in string) : 
        print( 0 )
        return
    
    # For a integer all of its multiples are equal to cherr [ 1 operation ]
    for x in range(2, length+1) :
        valid = True

        for multiple in range(x, length+1, x) :
            if string[ multiple-1 ] != cherr : 
                valid = False 
                break
        
        if valid :
            print(1)
            print(x)
            return
    # always possible to make it equal using 2 operations
    print(2)
    print(length, length-1)


testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
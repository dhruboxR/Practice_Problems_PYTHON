# https://codeforces.com/contest/1536/problem/B
import sys
input = sys.stdin.readline

#   FIND THE MINIMUM POSSIBLE STRING ,
#     - That is not present as a substring in the given string

#        Check len 1 : a, b, c, ....., z
#        Check len 2 : aa, ab, ac, ad, ....., az
#        Check len 3 : aaa, aab, aac, aad, ....., aaz, aba, abc, abd, ...., abz, ...., aca, acb, ..., acz

#        Checking combination till length 3 is enough [ n <= 1000 ]

def solve():
    n = int( input() )
    s = input().strip()

    # ord('a')  -> 97, ord('b')  -> 98, ord('z')  -> 122 
    # It basically converts a character → its integer code. TypeCast -> chr(i)

    # length 1
    for i in range( ord('a'), ord('z')+1 ) :
        current = chr(i)

        if current not in s :
            print( current )
            return
    
    # length 2
    for i in range( ord('a'), ord('z')+1 ) :
        for j in range( ord('a'), ord('z')+1 ) :
            current = chr(i) + chr(j)

            if current not in s :
                print( current )
                return
            
    # legnth 3
    for i in range( ord('a'), ord('z')+1 ) :
        for j in range( ord('a'), ord('z')+1 ) :
            for k in range( ord('a'), ord('z')+1 ) :
                current = chr(i) + chr(j) + chr(k)

                if current not in s :
                    print( current )
                    return

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
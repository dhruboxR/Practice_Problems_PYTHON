import sys
input = sys.stdin.readline

def solve():
    length = int( input() )
    source = list( map(int, input().split()) )

    mx = float( '-inf' )    # set value to negative infinity

    # find the maximum XOR value 
    for i in range(length) :
        for j in range(length) :
            currValue = source[ i ] ^ source[ j ]
            mx = max( mx, currValue )
    
    print( mx )

testCase = int( input() ) if True else 1
for _ in range (testCase) :
    solve()

# the constraints are low n(2 ≤ n ≤ 3105) -> O( n2 ) = 9e6 [ we can go up to 1e9 !! ] 

#   We have an array a=[a1,a2,a3,…,an]
#   Suppose we performed the operations from left to right, to see how operations affect the array.

#   After the first operation, the array becomes: 
#       a = [ a2 ⊕ a1 , a3 ⊕ a1, ......, an ⊕ a1 ]      -> Note that the first element was removed.

#   After the second operation, the array becomes 
#       a = [ (a3⊕a1)⊕(a2⊕a1), ....... ,(an⊕a1)⊕(a2⊕a1) ]

#   This is the same as a=[a3⊕a2,…,an⊕a2]

#           XOR PROPERTIES :
#               5 ⊕ 5 = 0 || x1 ⊕ x2 = 0

#               (a3⊕a1) ⊕ (a2⊕a1)
#               => a3 ⊕ a1 ⊕ a2 ⊕ a1    [ a1 negates each other out ]
#               remains => a3 ⊕ a2

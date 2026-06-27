# https://codeforces.com/problemset/problem/1692/F

import sys
input = sys.stdin.readline

"""
    Only the last digit matters because we only care whether the sum ends with 3. So, 
        - Replace eveery number by number % 10 
        - We only have 10 possible digits[ 0-9 ]

    Also we never need more than 3 occurances fo the same last digit, 
    Since we are choosing only 3 number
"""

def solve():
    n = int( input() )
    freq = {}

    source = list(map(int, input().split()))
    temp = [] 

    for integer in source : 
        mod = integer % 10 
        
        if(freq.get(mod, 0)) < 3 :
            temp.append(mod)
            freq[ mod ] = freq.get(mod, 0) + 1
    
    # B R U T E F O R C E 

    for i in range( len(temp) ) : 
        a = temp[ i ]; 
        
        for j in range( len(temp) ) : 
            if j == i : continue
            b = temp[ j ]

            for k in range( len(temp) ) : 
                if k == i or k == j : continue 
                c = temp[ k ]

                if (a+b+c) % 10 == 3 : 
                    print( "yes" )
                    return
    
    print( "no" )



testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
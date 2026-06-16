# https://codeforces.com/problemset/problem/2236/D

import sys
input = sys.stdin.readline


#    n = 9, k = 2 
#    1 2 3   7   10 11   15 17 18


#   If there are 2 distinct elements present in any block egor will win 
#   If there are only 1 distinct element then 
#   the size of that block should be even for egor to win

def solve():
   n, k = map(int, input().split())
   source = sorted(list(map(int, input().split())))

   blocks = []  # list for storing the blocks 
   temp = [ source[ 0 ] ]

   for i in range(1, n) :
       if source[ i ] - source[ i-1 ] <= k :
           temp.append( source[ i ] )
       else :
           blocks.append( temp )
           temp = [ source[ i ] ]
   
   blocks.append( temp )
    
    # Check Function 
   def distinct(curr) :
       s = set(curr)        # distinct elements in this block 
       
       if len(s) == 1 and len(curr) % 2 == 0 :
           return True
       
       return len(s) > 1
   
   for block in blocks :
       if distinct(block) : 
           print( "yes" )
           return
    
   print( "no" )
         
testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
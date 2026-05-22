# https://codeforces.com/problemset/problem/1881/D

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = 1000000+5               # 1e6 + 5
primes = []                 # list to store the prime numbers
markPrime = [True] * N      # mark the prime numbers 

def generatePrimes() :
    markPrime[ 0 ] = markPrime[ 1 ] = False
    
    for i in range(2, N) :
        if markPrime[ i ] :
            primes.append( i )

            for j in range(i*i, N, i) :
                markPrime[ j ] = False

def solve():
    length = int( input() )
    primeFreq = {}          # dictionary to store the frequency of the primes

    numbers = list( map(int, input().split()) )

    for value in numbers :

        for divisor in primes :
            if divisor * divisor > value : break        # no need to check further

            while value % divisor == 0 :
                value //= divisor
                primeFreq[ divisor ] = primeFreq.get(divisor, 0) + 1
        
        # the reamaining value is a prime number
        if value > 1 : primeFreq[ value ] = primeFreq.get(value, 0) + 1
    
    # equal division of the divisors 
    for div,frequency in primeFreq.items() :
        if frequency % length :
            print( "NO" )
            return
    
    print( "YES" )

generatePrimes()

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
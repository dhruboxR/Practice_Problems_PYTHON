#  https://codeforces.com/contest/2267/problem/C

import sys
import math
input = sys.stdin.readline

"""
    - We don't check whether any array element is divisible by X 
        - We check whether it is divisible by any individual prime factor of X 
            
        1. Find all distinct prime factors of x 
        2. For each array element, check which of those prime factors divide it 
        3. Maintain a separate sum for each prime factor, addng every divisible element to it's sum 
        4. The maximum of these sum is the answer 
"""
# Generate primes upto N. The maximum value for N can be (3 X 10^5)
N = 3 * 10**5  

primes = [] 
mark_prime = [True] * N

def generate_primes() :   
    mark_prime[0] = mark_prime[1] = False 

    for i in range(2, N) : 
        if mark_prime[i] : 
            primes.append(i) 

            for j in range(i*i, N, i) : 
                mark_prime[j] = False 

def solve() : 
    n, x = map(int, input().split()) 
    factors_x = [] 

    # Prime factorize x 
    for div in primes : 
        if div*div > x : break 

        if x % div == 0 : 
            factors_x.append(div) 

            while x % div == 0 : x //= div 

    if x > 1 : factors_x.append(x) 

    src = list(map(int, input().split())) 

    total = {}  # dictionary to store score for individual prime factors of X 

    for i in range(n) : 
        for div in factors_x : 
            if src[i] % div == 0 : 
                total[ div ] = total.get(div, 0) + src[i]; 

    answer = 0 
    for fact, score in total.items() : answer = max(answer, score)

    print(answer) 

testCase = int(input()) if True else 1

generate_primes() 

for _ in range(testCase):
    solve()
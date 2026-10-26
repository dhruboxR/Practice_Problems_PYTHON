# https://codeforces.com/problemset/problem/2276/C
import sys
import math
input = sys.stdin.readline

"""
1. Prefix Sum modulo k (pref[i]):
       Let S be the original array. The prefix sum array `pref` is defined as:
           pref[i] = (S[0] + S[1] + ... + S[i-1]) mod k
       
       Mathematical Property: 
       If two prefix sums at different indices have the exact same remainder modulo k, 
       i.e., pref[j] == pref[i] (where j < i), then the subarray sum from index j to i-1 
       is a multiple of k:
           (pref[i] - pref[j]) mod k = 0  ==>  Subarray sum is divisible by k.

2. Gap / Distance Constraint (i - k - 1):
       The problem enforces a structural or positional constraint between the two endpoints 
       of the subarray. Instead of considering all pairs (j, i), we maintain a sliding window 
       or separation gap of size `k + 1`, ensuring that only valid pairs meeting the distance 
       criterion are counted.

3. Frequency Array (freq):
       Acts as a hash/frequency map of past prefix sum remainders. When `pref[i]` is evaluated, 
       we look up how many times its exact remainder has previously appeared within the valid 
       distance window, accumulating those counts into the final `answer`.
"""

def solve():
    n, k = map(int, input().split()) 
    source = list(map(int, input().split())) 
    pref = [0] * (n+1) 

    # store the prefix sum modulo k up to index i-1 
    for i in range(n) :
        pref[i+1] = (pref[i] + source[i]) % k 

    answer = 0 
    freq = [0] * (n+1)  # track the freq of each prefixSum rem encountered 

    # iterate with a gap constraint of k+1 
    for i  in range(k+1, n+1) : 
        valid_idx = i - k - 1 
        if valid_idx >= 0 : 
            freq[ pref[valid_idx] ] += 1

        # matching remainder frequencies to count the valid subarray 
        answer += freq[ pref[i] ] 

    print(answer) 

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
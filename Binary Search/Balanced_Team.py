import sys
import math
input = sys.stdin.readline

def solve():
    n = int( input() )
    nums = list(map(int, input().split()))

    nums.sort()
    mxTeams = float('-inf')

    for i in range(n) : 
        target = nums[i] + 5
        low = i+1 
        high = n-1 
        valid_end = i   # last index where nums[j] <= nums[i]+5

        while low <= high : 
            mid = low + (high - low) // 2

            # valid element found try to find a larger index 
            if nums[ mid ] <= target : 
                valid_end = mid 
                low = mid + 1 
            else : 
                high = mid - 1  # difference is > 5 : search the left half 

        mxTeams = max(mxTeams, valid_end - i + 1)

    print(mxTeams) 

solve()
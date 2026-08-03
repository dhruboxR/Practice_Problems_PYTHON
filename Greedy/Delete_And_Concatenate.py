import sys
import math
input = sys.stdin.readline

"""
1. Subtract c from every element. Now every operation has zero cost.

2. Let need = ceil(n / 2).

3. Count the number of positive elements (p).
"""

def solve():
    n, cost = map(int, input().split())
    arr = list(map(int, input().split())) 

    # TRANSFORM THE ARRAY 
    arr = [x - cost for x in arr]

    need = (n + 1) // 2
    positive = 0

    for x in arr : 
        if x > 0 : 
            positive += 1

    # sort the array in descending order 
    arr.sort( reverse = True )

    score = sum(arr [:max(need, positive)])
    print( score )

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

"""
Case 1:
--------
    If p >= need,
    keep all positive elements.

    Reason:
        Every positive element increases the answer, and we can always pair
        the unwanted (non-positive) elements among them so that only the
        positive values contribute.

Case 2:
--------
    If p < need,we don't have enough positive elements.

    Even after pairing every negative with a positive (whenever possible),
    we are still forced to let some negative values contribute because
    at least 'need' elements must remain in the final score.

    So we choose the least harmful negatives (the largest non-positive
    values) until we have exactly 'need' contributing elements.

Answer:
--------
    Sort the transformed array in descending order and sum the first

        max(need, p)

    elements.

    Time: O(n log n)
"""
import sys
input = sys.stdin.readline

# n = a + b 
# a is a palindrome 
# b is divisible by 12

def checkPalindrome( val ) :
    temp = str(val)

    l, r = 0, len(temp)-1
    while l < r :
        if temp[ l ] != temp[ r ] : return False
        else :
            l += 1
            r -= 1
    return True

def solve():
    value = int( input() )

    for b in range((value//12)*12, -1, -12) :
        a = value - b 
        if checkPalindrome(a) :
            print(a, b)
            return
    
    print(-1)

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()

import sys
import math
input = sys.stdin.readline

def solve():
    n, p = map(int, input().split()) 
    ones = n // 2
    zeros = n - ones 

    if(ones + zeros - 2 < p) :      # not possible 
        print(-1)
        return
    
    if(ones + zeros - 2 == p) :     # satisfies requirements no changes needed 
        print("1" * ones + "0" * zeros)
        return 

    """
    Else we need to construct the final string 
        - place the extra 0's and 1's at the beginning 
        - then the rest all together 
    """

    charList = [] 

    while(ones + zeros - 2 > p) : 
        if not charList : 
            charList += "0"
            zeros -= 1
        else : 
            if charList[-1] == "1" : 
                charList.append("0")
                zeros -= 1 
            else : 
                charList.append("1")
                ones -= 1

    # FINAL CHECK AND OUTPUT 
    if ones + zeros - 2 < p : 
        if charList[-1] == "0" : 
            for _ in range(zeros): charList.append("0")
            for _ in range(ones) : charList.append("1")
        else : 
            for _ in range(ones) : charList.append("1")
            for _ in range(zeros): charList.append("0")
    else : 
        if charList[-1] == "0" : 
            for _ in range(ones) : charList.append("1")
            for _ in range(zeros): charList.append("0")
        else : 
            for _ in range(zeros): charList.append("0")
            for _ in range(ones) : charList.append("1")

    string = "".join( charList )
    print(string)

testCase = int(input()) if True else 1
for _ in range(testCase):
    solve()
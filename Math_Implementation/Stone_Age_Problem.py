# https://codeforces.com/problemset/problem/1679/B

def solve() :
    n, q = map( int, input().split() )
    arr = list( map(int, input().split()) )

    totalSum = sum( arr )

    valQ = []       # Dictionary to store the value and the last Query for the value
    valQ = [[x, 0] for x in arr]
    
    track = [ -1, -1 ]  # second query value, and QueryNo

    for i in range(1, q+1) :
        query = list( map(int, input().split()) )
        qtype = query[ 0 ]

        if qtype == 1 :
            idx, val = query[ 1 ], query[ 2 ]
            idx -= 1        # 0 based indexing

            if valQ[ idx ][ 1 ] > track[ 1 ] :     # valQ has the latest update
                totalSum += val - valQ[ idx ][ 0 ]
                print( totalSum )

                valQ[ idx ][ 0 ] = val      # update the value
                valQ[ idx ][ 1 ] = i        # update the QueryNo
            else :
                # track has the latest update
                totalSum += val - track[ 0 ]
                print( totalSum )

                valQ[ idx ][ 0 ] = val
                valQ[ idx ][ 1 ] = i
        else :
            val = query[ 1 ]
            
            track[ 0 ] = val
            track[ 1 ] = i

            totalSum = val * n
            print( totalSum )

testCase = 1
for _ in range( testCase ) : 
    solve()
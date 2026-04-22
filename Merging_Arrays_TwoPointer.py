# link : https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

def merge(a, b) :
    
    idx1, idx2 = 0, 0
    res = []                # Result list, initially empty 

    # we iterate till we reach the end of one array

    while idx1 < len(a) and idx2 < len(b) :
        if a[ idx1 ] < b[ idx2 ] :
            res.append( a[idx1] )
            idx1 += 1
        else :
            res.append( b[idx2] )
            idx2 += 1

    # insert elements from the other array 
    while idx1 < len(a) : 
        res.append( a[idx1] )
        idx1 += 1

    while idx2 < len(b) :
        res.append( b[idx2] )
        idx2 += 1

    return res


n, m = map( int, input().split() )

a = list( map(int, input().split()) ) 
b = list( map(int, input().split()) )

# call the func, store the result
result = merge(a, b)
print( *result )
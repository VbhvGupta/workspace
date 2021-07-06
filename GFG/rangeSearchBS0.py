def searchRange( A, B):
    ans = [-1,-1]
    end = len(A)-1
    start = 0
    mid = 0
    while start <= end :
        mid = (start+end) // 2
        if A[mid] < B :
            start = mid + 1
        elif A[mid] > B :
            end = mid - 1
        else :
            end = mid-1
            ans[0] = mid

    start = ans[0]
    end = len(A)-1
    while start <= end :
        mid = (start + end) // 2
        if A[mid] < B :
            start = mid + 1
        elif A[mid] > B :
            end = mid - 1
        else :
            start = mid+1
            ans[1] = mid
    return ans

A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
B = 10
print(searchRange(A,B))

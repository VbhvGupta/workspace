class Solution:
    def searchRange(self, A, B):
        ans = [-1,-1]
        ln = len(A)-1
        def search(A,B,start,end) :
            nonlocal ans
            if start > end : return
            mid = (start+end)//2
            if A[mid] == B :
                if ans == [-1,-1] :
                    ans.clear()
                    ans = [mid,mid]
                else :
                    ans[0] = min(ans[0],mid)
                    ans[1] = max(ans[1],mid)
                search(A,B,start,mid-1)
                search(A,B,mid+1,end)
            elif A[mid] > B :
                search(A,B,start,mid-1)
            elif A[mid] < B :
                search(A,B,mid+1,end)
        search(A,B,0,ln)
        return ans

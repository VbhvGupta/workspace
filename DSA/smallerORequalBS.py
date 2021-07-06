class Solution:
    def solve(self, A, B):
        ans = 0
        def find(A,B) :
            nonlocal ans
            if not A : return
            mid = len(A)//2
            if A[mid] <= B :
                ans+=mid+1
                if len(A) > 1: find(A[mid+1:],B)
            else :
                find(A[:mid],B)

        find(A,B)
        return ans

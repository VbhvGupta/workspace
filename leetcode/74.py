class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        m = len(matrix)
        n = len(matrix[0])
        
        def bin_Search(l,r) :
            if l<=r :
                mid = (l+r)//2
                num = matrix[mid//n][mid%n]
                if num == target :
                    return True
                if num < target :
                    return bin_Search(mid+1,r)
                return bin_Search(l,mid-1)
            else:
                return False
        
        return bin_Search(0,m*n-1)
                
                
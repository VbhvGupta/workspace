class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0 :
            return [num*num for num in nums]
        
        if nums[-1] < 0 :
            return [num*num for num in nums][::-1]
        
        def bin_search(l,r) :
            if l==r :
                return l
            if l+1 == r :
                return l if nums[l]>=0 else r
            mid = (l+r)//2
            if nums[mid] < 0 :
                return bin_search(mid+1 , r)
            return bin_search(l,mid)
        
        n = len(nums)-1
        frst_postv = bin_search(0,n)
        
        lft = [i*i for i in nums[:frst_postv][::-1] ]
        rght = [i*i for i in nums[frst_postv:] ]
        
        i,j,k=0,0,0
        while i < frst_postv and j < n-frst_postv+1 :
            if lft[i] < rght[j] :
                nums[k]=lft[i]
                i+=1
            else :
                nums[k]=rght[j]
                j+=1
            k+=1
        while i < frst_postv :
            nums[k] = lft[i]
            k+=1
            i+=1
        while j < n-frst_postv+1 :
            nums[k] = rght[j]
            k+=1
            j+=1
            
        return nums
        
        
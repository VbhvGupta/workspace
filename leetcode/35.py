class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binSearch(l , r) :
            if l == r :
                return l if nums[l] == target else (l if nums[l] > target else l+1)
            
            mid = (l+r)//2
            
            if nums[mid] == target :
                return mid
            elif nums[mid] < target :
                return binSearch(mid+1,r)
            else :
                return binSearch(l,mid)
        
        return binSearch(0,len(nums)-1)
            
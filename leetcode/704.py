class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bin_search( nums, l,r) :
            if l <= r :
                mid = (l+r) //2
                if nums[mid] == target :
                    return mid
                elif nums[mid] < target :
                    return bin_search(nums,mid+1,r)
                else :
                    return bin_search(nums,l,mid-1)
            else :
                return -1
        return bin_search(nums,0,len(nums)-1)
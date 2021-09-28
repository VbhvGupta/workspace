class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        prev = -999
        for i in range(len(nums)) :
            if nums[i] != prev:
                nums[count] = nums[i]
                count+=1
                prev = nums[i]
        return count
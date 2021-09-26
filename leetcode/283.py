class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = 0
        for i in range(len(nums))  :
            if nums[i] != 0 :
                nums[p1],nums[i] = nums[i] ,nums[p1]
                p1+=1
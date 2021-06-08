class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0 , len(nums)):
            num = nums[i]
            if (target - num) in nums and nums.index(target-num)!=i:
                    return [i,nums.index(target-num)]

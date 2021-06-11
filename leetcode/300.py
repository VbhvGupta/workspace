class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln ==0 :
            return 0
        ans = [1] * ln
        i = ln-1
        while i>=0 :
            for j in range(i+1, ln) :
                if nums[j] <= nums[i] :
                    pass
                else :
                    ans[i] = max(ans[i],1+ans[j])
            i-=1
        return max(ans)

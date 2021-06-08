class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        hash_mp = {}
        d = set()
        n = len(nums)
        for i in range(0,n) :
            hash_mp[nums[i]] = i
        for i in range(0,n-2) :              # x = nums[i]
            target = -1*nums[i]              # target = -1 * x
            for j in range(i+1 ,n):          # target =  y + z
                y = nums[j]
                if (target - y) in hash_mp and hash_mp[target-y] != i != j != hash_mp[target-y] :
                    if set((nums[i],nums[j],nums[hash_mp[target-y]])) not in d :
                        d.add(frozenset((nums[i],nums[j],nums[hash_mp[target-y]])))
                        ans.append([nums[i],nums[j],nums[hash_mp[target-y]]])
        return ans

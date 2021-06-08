class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        l1 = {}
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)) :
                if (nums1[i]+nums2[j]) not in l1 :  # O(n^2)
                    l1[(nums1[i]+nums2[j])] = 0
                l1[(nums1[i]+nums2[j])] += 1
        l2 = {}
        for i in range(0,len(nums3)) :
            for j in range(0,len(nums4)) :
                if (nums3[i]+nums4[j]) not in l2 :  # O(n^2)
                    l2[(nums3[i]+nums4[j])] = 0
                l2[(nums3[i]+nums4[j])] += 1

        ans = 0
        for a in l1 :
            if (-1*a) in l2 :
                ans += (l1[a]*l2[-1*a])
        return ans

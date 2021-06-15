class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)-1
        if ln == 0 :
            return
        i=ln
        flag = False
        for i in range(ln,0,-1):
            if nums[i-1] < nums[i] :
                flag = True
                min_ = nums[i-1]
                for j in range(ln,i-1,-1):
                    if nums[j] > min_ :
                        nums[j],nums[i-1] = nums[i-1],nums[j]
                        break
                print(nums)
                print(nums[i],'i='+str(i))
                break
        if flag == False :
            nums.sort()
        else :
            self.sort(i,nums,ln)

    def sort(self,l,nums,ln):
        for i in range(l+1,ln+1):
            key=nums[i]
            j=i-1
            while key<nums[j] and j>=l:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1] = key


        

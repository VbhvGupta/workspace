class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1 :
            return "1"
        lst = self.countAndSay(n-1)
        num = lst[0]
        count = 0
        ans = ""
        for i in range(len(lst)) :
            if num == lst[i] :
                count+=1
            else :
                ans+=str(count)+str(num)
                count = 1
                num = lst[i]
        ans+=str(count)+str(num)
        return ans
                

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev=s[0]
        temp_count = 1
        lst_count = []
        for i in range(1,len(s)) :
            if s[i] != prev :
                prev = s[i]
                lst_count.append(temp_count)
                temp_count = 1
            else :
                temp_count += 1
        lst_count.append(temp_count)

        ans = 0
        for i in range(1,len(lst_count)) :
            ans += min(lst_count[i-1],lst_count[i])
        return ans

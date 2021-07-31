class Solution:
    def longestPalindrome(self, s: str) -> str:
        ln = len(s)
        i = ln
        while i > 0 :
            for j in range(0,ln-i+1) :  #  O(n^2)
                s1 = s[j:j+i]
                if s1 == s1[::-1] :
                    return s1
            i-=1

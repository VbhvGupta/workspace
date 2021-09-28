class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack) :
            return -1
        if len(needle) == len(haystack) :
            return 0 if needle == haystack else -1
        
        window = len(needle) # 1
        for i in range(0,len(haystack)-window+1) : # (0,2)
            if haystack[i:i+window] == needle :
                return i
        return -1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False 
        sc = Counter(s)
        tc = Counter(t)
        return sc == tc == sc and tc
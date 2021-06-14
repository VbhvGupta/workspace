class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        i = 0
        strng = [None]*len(s)
        while i<len(s) :
            strng[indices[i]] = s[i]
            i+=1

        return ''.join(strng)

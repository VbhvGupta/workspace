class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'I': 1,'V': 5,'X': 10,'L' :50,'C':  100,'D': 500,'M' :1000}
        prev = 'Z'
        value = 0
        for i in range(len(s)-1,-1,-1) :
            if s[i]=='I' and prev in 'VX' or s[i]=='X' and prev in 'LC' or s[i]=='C' and prev in 'DM' :
                value -= mp[s[i]]
            else :
                value += mp[s[i]]
            prev = s[i]
        return value
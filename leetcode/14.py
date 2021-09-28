class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs : return ''
        if len(strs) == 1: return strs[0]
        pre = ''
        k=0
        while True :
            if k >= len(strs[0]) :
                return pre
            prev = strs[0][k]
            for i in range(1,len(strs)) :
                if k >= len(strs[i]) or strs[i][k] != prev :
                    return pre
            pre += prev
            k+=1
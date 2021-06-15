class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ln = len(s)
        lst = [False] * ln
        lst.insert(0,True)

        for i in range(1,ln+1) :
            for w in wordDict :
                if lst[i-len(w)]  and s[:i].endswith(w) :
                    lst[i]=True
        return lst[-1]

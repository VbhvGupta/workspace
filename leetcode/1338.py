import math
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        m = {}
        ln = 0
        for el in arr :
            if el not in m :
                m[el] = 0
            m[el] += 1
            ln+=1

        ln = math.ceil(ln/2)

        m=dict(sorted(m.items(), key=lambda item: item[1], reverse = True ))
        print(m)
        ans = 0
        sum_ = 0
        for key in m:
            if sum_+m[key] < ln :
                sum_+=m[key]
                ans+=1
            else :
                return ans+1

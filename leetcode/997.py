class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust :
            if n == 1 :
                return 1
            else :
                return -1
        left = []
        right = []
        count_map = {}
        for i in range(0,len(trust)) :
            left.append(trust[i][0])
            right.append(trust[i][1])
            if trust[i][1] not in count_map :
                count_map[trust[i][1]]=0
            count_map[trust[i][1]]+=1
        canbe = list(set(right) - set(left))
        for el in count_map :
            if el in canbe and count_map[el] == n-1 :
                return el
        return -1

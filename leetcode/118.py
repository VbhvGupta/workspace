class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        ans = [[1]]
        for i in range(1,numRows) :
            prev = [0]+ans[-1]+[0]
            temp = list()
            for j in range(1,len(prev)) :
                temp.append(prev[j]+prev[j-1])
            prev.clear()
            prev = [0]+[temp]+[0]
            ans.append(temp)
        return ans
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        
        if m*n != r*c :
            return mat
        
        _1d = []
        for i in range(m) :
            _1d.extend(mat[i])
        
        res = [[0]*c for _ in range(r)]
        
        k = 0
        for i in range(r) :
            for j in range(c) :
                res[i][j] = _1d[k]
                k+=1
        return res
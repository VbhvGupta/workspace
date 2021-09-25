class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        '''
         00 01 02   03 04 05   06 07 08
         10 11 12   13 14 15   16 17 18 
         20 21 22   23 24 25   26 27 28
         
         30 31 32   33 34 35   36 37 38
         40 41 42   43 44 45   46 47 48
         50 51 52   53 54 55   56 57 58
          
         60 61 62   63 64 65   66 67 68
         70 71 72   73 74 75   76 77 78
         80 81 82   83 84 85   86 87 88
         
        '''
        mp = {}
        
        for i in range(9) :
            for j in range(9) :
                if board[i][j] != '.' :
                    if board[i][j] not in mp :
                        mp[board[i][j]] = [ ]
                    else :
                        for k in range(len(mp[board[i][j]])) :
                            l,r = mp[board[i][j]][k][0], mp[board[i][j]][k][1]
                            if l  == str(i) or r == str(j) : 
                                #print("ok")
                                return False
                            if i//3 == int(l)//3 and j//3 == int(r)//3 :
                                #print("OKAY : ",l,r)
                                return False
                    mp[board[i][j]].append(str(i)+str(j))
                    #print(mp)
        return True
                            
                
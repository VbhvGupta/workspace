
class Solution:

    #Function to find minimum time required to rot all oranges.
	def orangesRotting(self, grid):
	    itr = 0
	    n = len(grid)
	    m = len(grid[0])
	    once = False
	    def rot_cell(x,y,k) :
            if grid[x][y] == 1 and k ==1:
                grid[x][y] = 2
                return 1
            if grid[x][y] == 1 and k==0 :
                grid[x][y] = -1
                return 1
            return 0

	    def rot_neighbors(i,j) :
	        change = 0

	        if  0 <= i-1 < n and 0 <= j < m :
	            change += rot_cell(i-1,j,1)

	        if  0 <= i+1 < n and 0 <= j < m :
	            change += rot_cell(i+1,j,0)

	        if  0 <= i < n and 0 <= j-1 < m :
	            change += rot_cell(i,j-1,1)

	        if  0 <= i < n and 0 <= j+1 < m :
	            change += rot_cell(i,j+1,0)

            return 1 if change > 0 else 0

	    while True :
	        changes = 0
	        ones = False
	        # make changes here
	        for i in range(0,n) :
	            for j in range(0,m) :
	                if grid[i][j] == -1 :
	                    grid[i][j] = 2
	                else :
    	                if grid[i][j] == 0 or grid[i][j] == 1 :
    	                    if grid[i][j] == 1:
    	                        ones = True
    	                else :
    	                    changes += rot_neighbors(i,j)
	        #print(grid)
	        if changes == 0:
	            break
	        itr += 1
	    return -1 if ones else itr

#{
#  Driver Code Starts

from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends

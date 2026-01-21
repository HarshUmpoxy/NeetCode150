# Always take care of the datatype in the grid

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==-1 or grid[i][j]=='0':
                return
            grid[i][j]=-1
            for d in directions:
                dfs(i+d[0], j+d[1])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ans = ans + 1
                    dfs(i, j)
        
        return ans


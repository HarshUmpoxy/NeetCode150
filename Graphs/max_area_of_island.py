class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==-1 or grid[i][j]==0:
                return 0
            grid[i][j]=-1
            ans = 1
            for d in directions:
                ans = ans + dfs(i+d[0], j+d[1])
            return ans
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans = max(ans,dfs(i,j))
        
        return ans


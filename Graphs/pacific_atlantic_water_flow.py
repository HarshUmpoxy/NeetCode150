class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        atlantic, pacific = set(), set()

        def dfs(r, c, visit, prevHeight): # prevHeight helps us determine the next decision
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visit or heights[r][c]<prevHeight:
                return
            visit.add((r,c)) #Syntax is imp
            dfs(r+1,c,visit, heights[r][c])
            dfs(r,c+1,visit, heights[r][c])
            dfs(r-1,c,visit, heights[r][c])
            dfs(r,c-1,visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pacific, 0)
            dfs(ROWS - 1, c, atlantic, 0)

        for r in range(ROWS):
            dfs(r, 0, pacific, 0)
            dfs(r, COLS - 1, atlantic, 0)
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in atlantic and (i,j) in pacific:
                    res.append([i,j])
        
        return res
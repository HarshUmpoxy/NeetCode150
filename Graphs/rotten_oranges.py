# Classical Multi-source bfs problem
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = collections.deque()
        
        minutes = 0
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh = 1 + fresh
                if grid[i][j]==2:
                    q.append((i,j))

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        while fresh >= 1 and q: # q is important to avoid inf loop incase of -1 return
            print(fresh)
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dx, dy in directions: #Indentation is imp, understand the logic
                    nx = r + dx
                    ny = c + dy
                    if nx>=0 and nx<n and ny>=0 and ny<m and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        fresh = fresh - 1
                        q.append((nx, ny))
            minutes = minutes + 1
        
        return minutes if fresh == 0 else -1
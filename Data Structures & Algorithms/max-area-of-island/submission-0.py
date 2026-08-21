class Solution:
    def isValid(self, row, col):
        return row in range(self.rows) and col in range(self.cols)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        visited = set()

        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        def dfs(i,j):
            visited.add((i,j))
            area = 1
            for r, c in directions:
                nr = r + i
                nc = c + j
                if self.isValid(nr, nc) and (nr,nc) not in visited and grid[nr][nc] == 1:
                    area += dfs(nr,nc)

            return area
                    
        ans = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    ans = max(ans, dfs(i,j))

        return ans
class Solution:
    def isValid(self, i, j):
        # outa bound
        return (
            0 <= i < self.ROWS
            and 0 <= j < self.COLS
        )
            
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        res = 0
        def dfs(r,c):
            visited.add((r,c))
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if (self.isValid(nr, nc)
                    and (nr,nc) not in visited 
                    and grid[nr][nc] == "1" 
                    ):
                    dfs(nr,nc)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if (
                    (r,c) not in visited
                    and grid[r][c] == "1"
                ):
                    dfs(r,c)
                    res += 1

        return res


                    



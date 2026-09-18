class Solution:
    def isValid(self, r,c):
        return r in range(self.ROWS) and c in range(self.COLS)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_orange = 0
        minutes = 0
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_orange += 1
                if grid[i][j] == 2:
                    queue.append((i,j))  

        while queue and fresh_orange > 0:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if self.isValid(nr,nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        queue.append((nr,nc))
                        fresh_orange -= 1
            minutes += 1  

        return minutes if fresh_orange == 0 else -1
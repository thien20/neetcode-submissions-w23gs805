class Solution:
    def isValid(self, row, col):
        if row < 0 or col < 0 or row >= self.ROW or col >= self.COL:
            return False
        if self.visited[row][col]:
            return False
    
        return True

    def dfs(self, row, col, i):
        if i == len(self.word):
            return True
        if not self.isValid(row,col):
            return False
        if self.word[i] != self.board[row][col]:
            return False

        # move 4 direction if we find that word and mark the visted
        self.visited[row][col] = True
        for dr, dc in self.directions:
            new_row = row + dr
            new_col = col + dc

            if self.dfs(new_row, new_col, i+1):
                return True
        self.visited[row][col] = False

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.N = [-1,0]
        self.S = [1,0]
        self.W = [0,-1]
        self.E = [0,1]

        self.directions = [self.N, self.S, self.W, self.E]

        self.board = board
        self.word = word

        self.ROW = len(board)
        self.COL = len(board[0])

        self.visited = [[False for _ in range(self.COL)] for _ in range(self.ROW)]
        # trying all cells
        for row in range(self.ROW):
            for col in range(self.COL):
                if self.dfs(row, col, 0):
                    return True

        return False

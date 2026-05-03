class Solution:
    def backtracking(self, n, row, board):
        if row == n:
            return self.res.append(["".join(thatrow) for thatrow in board])

        for col in range(len(self.cols)):
            if self.cols[col]:
                continue
            if self.fwd_diag[row + col]:
                continue
            if self.bwd_diag[row - col + (n-1)]:
                continue

            # choose
            self.board[row][col] = "Q"
            self.cols[col] = True
            self.fwd_diag[row + col] = True
            self.bwd_diag[row - col + (n-1)] = True

            # explore
            self.backtracking(n, row+1, self.board)

            # undo
            self.board[row][col] = "."
            self.cols[col] = False
            self.fwd_diag[row + col] = False
            self.bwd_diag[row - col + (n-1)] = False

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.cols = [False] * (n)
        self.fwd_diag = [False] * (2*n-1)
        self.bwd_diag = [False] * (2*n-1)

        self.board = [["."]*n for _ in range(n)]
        self.backtracking(n, 0, self.board)
        return self.res
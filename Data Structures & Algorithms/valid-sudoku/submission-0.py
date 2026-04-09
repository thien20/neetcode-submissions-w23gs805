class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1st 3 rows --> [stay, +3] - [stay, +3]
        # [0,0] - [2,2] --> box 1
        # [0,3] - [2,5] --> box 2
        # [0,6] - [2,8] --> box 3


        # 2nd 3 rows --> [+3, stay] - [+3, stay]
        # [3,0] - [5,2] --> box 4
        # [3,3] - [5,5] --> box 5
        # [3,6] - [5,8] --> box 6

        # 3rd 3 rows --> [+3, stay] - [+3, stay]
        # [6,0] - [8,2] --> box 7
        # [6,3] - [8,5] --> box 8
        # [6,6] - [8,8] --> box 9

        # acceptant criteria:
        # 1. check col
        # 2. check row
        # 3. check 3x3 box

        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False

                seen.add(board[row][i])

        for col in range(9):
            seen2 = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen2:
                    return False

                seen2.add(board[i][col])

        # 3x3 box --> complexity O(n^2) --> 81
        for box in range(9):
            seen3 = set()
            for i in range(3):
                for j in range(3):
                    row = (box//3) * 3 + i # 0 - 3 -6
                    col = (box%3) * 3 + j # 1,2 - 4,5 - 7,8
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen3:
                        return False

                    seen3.add(board[row][col])


        return True












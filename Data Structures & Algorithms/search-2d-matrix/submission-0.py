class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp = []
        for ma in matrix:
            temp.extend(i for i in ma)

        if target in temp:
            return True
        return False
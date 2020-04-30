from typing import List
class Solution:
    def __init__(self):
        self.col_len = 0
        self.row_len = 0
        self.max_s = 0
        self.matrix = None
    
    def get_max(self, r_i: int, c_i: int) -> None:
        pos_max = min(self.row_len - r_i, self.col_len - c_i)
        if self.max_s >= pos_max:
            return 0
        for i in range(1, pos_max + 1):
            row_list = self.matrix[r_i + i - 1][c_i:c_i + i]
            col_list = [self.matrix[x][c_i + i - 1] for x in range(r_i, r_i + i)]
            checker = row_list + col_list
            if not all(map(int, checker)):
                return
            self.max_s = max(self.max_s, i)

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.row_len = len(matrix)
        if not self.row_len:
            return 0
        self.col_len = len(matrix[0])
        self.matrix = matrix
        for r in range(self.row_len):
            for c in range(self.col_len):
                if matrix[r][c] == "1":
                    self.get_max(r, c)
        return self.max_s ** 2
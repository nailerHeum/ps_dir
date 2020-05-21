class Solution:
    def __init__(self):
        self.y = 0
        self.x = 0
        self.matrix = None
        self.count = 0
        self.checker = None
    def countSquare(self, n):
        for y in range(self.y - n + 1):
            for x in range(self.x - n + 1):
                if not self.checker[y][x]:
                    continue
                if not self.matrix[y][x]:
                    self.checker[y][x] = False
                    continue
                for t in self.matrix[y:y + n]:
                    if not all(t[x:x + n]):
                        self.count -= 1
                        self.checker[y][x] = False
                        break
                self.count += 1
    def countSquares(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.y = len(matrix)
        self.x = len(matrix[0])
        self.checker = [[True for x in range(self.x)] for y in range(self.y)]
        smaller = self.x if self.x < self.y else self.y
        self.count = sum([sum(x) for x in matrix])
        for i in range(2, smaller + 1):
            self.countSquare(i)
        return self.count
        

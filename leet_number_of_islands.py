from typing import List
class Solution:
    def __init__(self):
        self.lands = {}
        self.grid = None
        self.xlen = 0
        self.ylen = 0
    def init_lands(self):
        for i in range(self.xlen):
            self.lands[i] = []

    def dfs(self, tup):
        x, y = tup
        try:
            is_land = self.grid[x + 1][y] == '1' and not y in self.lands[x + 1]
            if is_land:
                self.lands[x + 1].append(y)
                self.dfs((x + 1, y))
        except:
            pass
        try:
            if x - 1 < 0:
                raise Exception()
            is_land = self.grid[x - 1][y] == '1' and not y in self.lands[x - 1]
            if is_land:
                self.lands[x - 1].append(y)
                self.dfs((x - 1, y))
        except:
            pass
        try:
            is_land = self.grid[x][y + 1] == '1' and not y + 1 in self.lands[x]
            if is_land:
                self.lands[x].append(y + 1)
                self.dfs((x, y + 1))
        except:
            pass
        try:
            if y - 1 < 0:
                raise Exception()
            is_land = self.grid[x][y - 1] == '1' and not y - 1 in self.lands[x]
            if is_land:
                self.lands[x].append(y - 1)
                self.dfs((x, y - 1))
        except:
            pass
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.xlen = len(grid)
        self.init_lands()
        try:
            self.ylen = len(grid[0])
        except:
            return 0
        answer = 0
        for x in range(self.xlen):
            for y in range(self.ylen):
                if grid[x][y] == '1' and not y in self.lands[x]:
                    self.lands[x].append(y)
                    answer += 1
                    self.dfs((x, y))
        return answer
sol = Solution()
sol.numIslands()
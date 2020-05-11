from typing import List

class Solution:
    def __init__(self):
        self.image = None
        self.new_color = 0
        self.x_len = 0
        self.y_len = 0
        self.original_color = 0
        self.visit_checker = None
        
    def check_coordi(self, sr, sc):
        return self.image[sr][sc] == self.original_color and not self.visit_checker[sr][sc]
    
    def fill_point(self, sr, sc):
        self.visit_checker[sr][sc] = True
        self.image[sr][sc] = self.new_color
        # right
        if sc < self.x_len - 1 and self.check_coordi(sr, sc + 1):
            self.fill_point(sr, sc + 1)
        # left
        if sc > 0 and self.check_coordi(sr, sc - 1):
            self.fill_point(sr, sc - 1)
        # top
        if sr > 0 and self.check_coordi(sr - 1, sc):
            self.fill_point(sr - 1, sc)
        # bottom
        if sr < self.y_len - 1 and self.check_coordi(sr + 1, sc):
            self.fill_point(sr + 1, sc)
        return
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.new_color = newColor
        self.x_len = len(image[0])
        self.y_len = len(image)
        self.visit_checker = [[False for _ in range(self.x_len)] for _ in range(self.y_len)]
        self.original_color = image[sr][sc]
        self.fill_point(sr, sc)
        return self.image
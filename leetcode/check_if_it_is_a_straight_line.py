from sys import float_info
from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        if x1 - x0 == 0:
            return all(map(lambda coor: coor[1] == y0, coordinates))
        default_inclination = (y1 - y0) / (x1 - x0)
        for i in range(1, len(coordinates)):
            x1, y1 = coordinates[i - 1]
            x2, y2 = coordinates[i]
            try:
                err = abs((y2 - y1) / (x2 - x1) - default_inclination)
            except:
                return False
            if err < float_info.epsilon:
                continue
            return False
        return True
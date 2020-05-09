class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        origin = 1
        while True:
            if origin ** 2 > num:
                return False
            if origin ** 2 == num:
                return True
            origin += 1

from itertools import combinations
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        for _ in range(k):
            i = 0
            while i < len(num) - 1:
                if num[i] > num[i + 1]:
                    break
                i += 1
            num = num[:i] + num[i + 1:]
        if not num:
            return "0"
        return str(int(num))
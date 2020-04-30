from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = [False] * len(nums)
        mem[0] = True
        for i in range(len(nums)):
            if not mem[i] or mem[i] == 0:
                continue
            max_j = min(mem[i], len(nums) - i - 1)
            for j in range(1, max_j + 1):
                if j + i == len(nums) - 1:
                    return True
                mem[j + i] = True
        

# O(n) solve
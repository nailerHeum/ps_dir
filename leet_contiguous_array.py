class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        mem = {0: 0}
        equal, maximum = 0, 0
        for i in range(len(nums)):
            equal += 1 if nums[i] else -1
            try:
                maximum = max(i - mem[equal], maximum)
            except:
                mem[equal] = i
        return maximum

sol = Solution()
print(sol.findMaxLength([0,0,1,0,0,0,1,1]))

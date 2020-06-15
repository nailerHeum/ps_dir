class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        answer = []
        if not nums:
            return []
        nums = sorted(nums)
        candis = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if not nums[i] % nums[j] and len(candis[i]) < len(candis[j]) + 1:
                    candis[i] = candis[j] + [nums[i]]
        return max(candis, key=lambda x: len(x))
                

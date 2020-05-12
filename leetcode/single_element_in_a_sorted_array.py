class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        while low < high:
            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    low = mid
                else:
                    high = mid - 1
            elif nums[mid] == nums[mid - 1]:
                if mid % 2 == 0:
                    high = mid
                else:
                    low = mid + 1
            else:
                return nums[mid]
            mid = (low + high) // 2
        return nums[mid]

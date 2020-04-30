from typing import List
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dupdict = {}
        for num in self.nums:
            if num in self.dupdict:
                self.dupdict[num] = False
                continue
            self.dupdict[num] = True
    def showFirstUnique(self) -> int:
        for i in range(len(self.nums)):
            if self.dupdict[self.nums[i]]:
                self.nums = self.nums[i:]
                return self.nums[0]
        self.nums = []
        return -1

    def add(self, value: int) -> None:
        if value in self.dupdict:
            self.dupdict[value] = False
            return
        self.dupdict[value] = True
        self.nums.append(value)
        return
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
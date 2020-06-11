from math import gcd
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        def change(done_idx, idx, tmp):
            while True:
                nums[idx], tmp = tmp, nums[idx]
                if done_idx == idx:
                    return
                idx = (idx + k) % len(nums)
        if k == 0:
            return
        loop_count = gcd(k, len(nums))
        for i in range(loop_count):
            change(i, (i + k) % len(nums), nums[i])
        return
                
        

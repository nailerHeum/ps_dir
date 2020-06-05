import random
class Solution:

    def __init__(self, w: List[int]):
        self.w_list = w
        self.w_dict = {}
        acc = 0
        for i, v in enumerate(w):
            if v == 0:
                continue
            acc += v
            self.w_dict[acc] = i
        self.max_v = acc
            

    def pickIndex(self) -> int:
        pi = random.randrange(1, self.max_v + 1)
        for k in self.w_dict.keys():
            if k >= pi:
                return self.w_dict[k]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        j_dict = dict(zip(J, [1] * len(J)))
        for s in S:
            if s in j_dict:
                count += 1
        return count
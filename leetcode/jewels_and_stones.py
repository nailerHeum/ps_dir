class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([x for x in S if x in dict(zip(J, [1] * len(J)))])
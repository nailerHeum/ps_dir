class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = ''.join(sorted(s1))
        len_s1 = len(s1)
        for i in range(len(s2) - len_s1 + 1):
            if sorted_s1 == ''.join(sorted(s2[i:i + len_s1])):
                return True
        return False

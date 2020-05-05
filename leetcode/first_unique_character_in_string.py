class Solution:
    def firstUniqChar(self, s: str) -> int:
        c_dict = {}
        for c in s:
            if c in c_dict:
                c_dict[c] = False
            else:
                c_dict[c] = True
        for i, c in enumerate(s):
            if c_dict[c]:
                return i
        return -1

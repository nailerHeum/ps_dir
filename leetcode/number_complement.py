class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join([str((int(x) + 1) % 2) for x in format(num, 'b')]), 2)
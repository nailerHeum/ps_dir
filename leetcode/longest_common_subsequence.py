class Solution:
    def __init__(self):
        self.result_dict = {}
        self.my_s = ''
        self.comp_s = ''
        
    def get_max_seq(self, my_i, comp_i):
        if (my_i, comp_i) in self.result_dict:
            return self.result_dict[(my_i, comp_i)]
        my = self.my_s[my_i:]
        comp = self.comp_s[comp_i:]
        max_seq = 0
        if not my or not comp:
            return 0
        for i in range(len(my)):
            if max_seq > len(my) - i:
                break
            if not my[i] in comp:
                continue
            comp_idx = comp.find(my[i])
            seq = self.get_max_seq(my_i + i + 1, comp_i + comp_idx + 1) + 1
            if max_seq < seq:
                max_seq = seq
        self.result_dict[(my_i, comp_i)] = max_seq
        return max_seq
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        max_s = 0
        if len(text1) >= len(text2):
            self.comp_s = text1
            self.my_s = text2
        else:
            self.comp_s = text2
            self.my_s = text1
        for i in range(len(self.my_s)):
            if max_s > len(self.my_s) - i:
                break
            if not self.my_s[i] in self.comp_s:
                continue
            comp_idx = self.comp_s.find(self.my_s[i])
            new_seq = self.get_max_seq(i + 1, comp_idx + 1) + 1
            if max_s < new_seq:
                max_s = new_seq
        return max_s
# abcdefghijklmnop
# maobcdefwgefw
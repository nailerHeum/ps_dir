class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_idx = 0
        while s:
            if not t:
                return False
            try:
                t_idx = t.index(s[0])
            except:
                return False
            t = t[t_idx + 1:]
            s = s[1:]
        return True
            

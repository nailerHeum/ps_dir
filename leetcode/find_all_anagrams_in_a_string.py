class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        sorted_p = ''.join(sorted(p))
        answer = []
        for i in range(len(s) - p_len + 1):
            if ''.join(sorted(s[i:i + p_len])) == sorted_p:
                answer.append(i)
        return answer 

class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        sorted_dict = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
        
        return ''.join([k * v for k, v in sorted_dict])
            

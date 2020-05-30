class Solution:
    def __init__(self):
        self.dislike_dict = {}
        self.checker = []
    def recur(self, key, color):
        print(key, color)
        if self.checker[key - 1] == color * -1:
            return False
        if self.checker[key - 1]:
            return True
        self.checker[key - 1] = color
        for new_key in self.dislike_dict[key]:
            if not new_key in self.dislike_dict:
                continue
            if not self.recur(new_key, color * -1):
                return False
        return True
        
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.checker = [0] * N
        dislike_dict = {}
        for a, b in dislikes:
            if a in dislike_dict:
                dislike_dict[a].append(b)
            else:
                dislike_dict[a] = [b]
            if b in dislike_dict:
                dislike_dict[b].append(a)
            else:
                dislike_dict[b] = [a]
        self.dislike_dict = dislike_dict
        for i in range(1, N + 1):
            if not self.checker[i - 1] and i in self.dislike_dict:
                if not self.recur(i, 1):
                    return False
        return True
        

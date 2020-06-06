class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_p = sorted(people, key=lambda x: x[0])
        answer = [None] * len(people)
        for h, k in sorted_p:
            tmp_idx = 0
            idx = 0
            while idx < len(answer):
                if answer[idx] is not None and answer[idx][0] < h:
                    idx += 1
                    continue
                if tmp_idx == k:
                    break
                tmp_idx += 1
                idx += 1
            answer[idx] = [h, k]
            
        return answer

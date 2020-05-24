class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        b_idx = 0
        answer = []
        b_len = len(B)
        if not B:
            return []
        for start, end in A:
            while b_len > b_idx and B[b_idx][1] < start:
                b_idx += 1
            if b_len == b_idx:
                break
            while b_len > b_idx and B[b_idx][0] <= end:
                b_s, b_e = B[b_idx]
                if start >= b_s and start <= b_e and end >= b_e:
                    answer.append([start, b_e])
                    b_idx += 1
                    continue
                if start <= b_s and end >= b_s and end <= b_e:
                    answer.append([b_s, end])
                    break
                if start <= b_s and end >= b_e:
                    answer.append([b_s, b_e])
                    b_idx += 1
                    continue
                if start >= b_s and end <= b_e:
                    answer.append([start, end])
                    break
        return answer
            

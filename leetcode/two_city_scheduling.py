class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_costs = sorted(costs, key=lambda x: abs(x[0] - x[1]), reverse=True)
        a_count, b_count = 0, 0
        N = len(costs) // 2
        answer = 0
        for a, b in sorted_costs:
            if a_count == N:
                answer += b
                continue
            if b_count == N:
                answer += a
                continue
            if a < b:
                answer += a
                a_count += 1
            else:
                answer += b
                b_count += 1
        return answer
            

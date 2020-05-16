from typing import List
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        local_max = 0
        local_min = 0
        glob_max = min(A)
        glob_min = min(A)
        for i in range(len(A)):
            if A[i] < A[i] + local_max:
                local_max += A[i]
            else:
                local_max = A[i]
            if A[i] < A[i] + local_min:
                local_min = A[i]
            else:
                local_min += A[i]
            if glob_max < local_max:
                glob_max = local_max
            if glob_min > local_min:
                glob_min = local_min
        print(glob_max, glob_min)
        if sum(A) == glob_min:
            return glob_max
        return glob_max if glob_max > sum(A) - glob_min else sum(A) - glob_min
    
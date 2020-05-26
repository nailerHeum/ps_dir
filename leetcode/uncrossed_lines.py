class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        len_a = len(A)
        len_b = len(B)
        arr = [[0] * (len_b + 1) for x in range(len_a + 2)]
        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if A[i - 1] == B[j - 1]:
                    arr[i][j] = 1 + arr[i - 1][j - 1]
                else:
                    arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
        return arr[len_a][len_b] 

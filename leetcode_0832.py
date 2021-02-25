class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range((len(A[i]) + 1) // 2):
                if A[i][j] == A[i][-1-j]:
                    A[i][j] ^= 1
                    if j != len(A)-1-j:
                        A[i][-1-j] ^= 1
        return A

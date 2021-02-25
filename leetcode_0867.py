class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trans_matrix = []
        for i in range(len(matrix[0])):
            temp_row = []
            for j in range(len(matrix)):
                temp_row += [matrix[j][i]]
            trans_matrix += [temp_row]
        return trans_matrix

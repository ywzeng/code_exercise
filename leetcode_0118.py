class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result_list = []
        for i in range(numRows):
            temp_level_list = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp_level_list += [1]
                else:
                    temp_level_list += [result_list[i-1][j-1]+result_list[i-1][j]]
            result_list += [temp_level_list]
        return result_list

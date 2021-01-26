class Solution:
    def grayCode(self, n: int) -> List[int]:
        result_list = [0]
        head = 1
        for i in range(n):
            for j in range(len(result_list)-1, -1, -1):
                result_list += [result_list[j] + head]
            head *= 2
        return result_list

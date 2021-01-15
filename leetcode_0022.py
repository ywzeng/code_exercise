class Solution_1:
    def __init__(self):
        self.result_list = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(n, '', 0, 0)
        return self.result_list
    
    def generate(self, n: int, generate_str: str, count_1: int, count_2: int) -> None:
        if count_1 > n or count_2 > n:
            return
        if count_1 == n and count_2 == n:
            self.result_list += [generate_str]
            return
        if count_1 >= count_2:
            self.generate(n, generate_str+'(', count_1+1, count_2)
            self.generate(n, generate_str+')', count_1, count_2+1)

class Solution_2:
    def __init__(self):
        self.result_list = []

    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(n, '', 0, 0)
        return self.result_list
    
    def generate(self, n: int, generate_str: str, count_1: int, count_2: int) -> None:
        if count_1 > n or count_2 > n:
            return
        if count_1 == n and count_2 == n:
            self.result_list += [generate_str]
            return
        if count_1 >= count_2:
            self.generate(n, generate_str+'(', count_1+1, count_2)
            self.generate(n, generate_str+')', count_1, count_2+1)

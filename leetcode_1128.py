class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """ 
        There are maybe one pair that has the same candidate. 
        For example, [[1,2],[1,2],[1,1],[1,2],[2,2]] has three pairs, namely three pairs of [1,2].
        We can use hash map. How to select the best key format to reflect the equivalence of [a, b] and [b, a].
        """
        from math import factorial
        temp_dict = {}
        key_dict = {}
        for item in dominoes:
            item = item[0]*10+item[1] if item[0]>item[1] else item[1]*10+item[0]
            temp_dict[item] = temp_dict.get(item, 0) + 1
            if temp_dict[item] > 1:
                key_dict[item] = 1
        pair_num = 0
        for key in key_dict:
            if temp_dict[key] > 1:
                pair_num += factorial(temp_dict[key]) // (factorial(2) * factorial(temp_dict[key]-2))
        return pair_num

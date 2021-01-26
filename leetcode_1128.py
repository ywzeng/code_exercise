class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """ 
        There are maybe one pair that has the same candidate. 
        For example, [[1,2],[1,2],[1,1],[1,2],[2,2]] has three pairs, namely three pairs of [1,2].
        We can use hash map. How to select the best key format to reflect the equivalence of [a, b] and [b, a].
        When calculating C(2_m), namely randomly select 2 items from m items, we get C(2_m)=m!/(2!*(m-2)!)=m*(m-1)/2!=m(m-1)/2.
        """
        from math import factorial
        temp_dict = {}
        for item in dominoes:
            item = item[0]*10+item[1] if item[0]>item[1] else item[1]*10+item[0]
            temp_dict[item] = temp_dict[item]+1 if item in temp_dict else 1
        pair_num = 0
        for key in temp_dict:
            # C(2_m)=m(m-1)/2. If m == 1, we get 1*0/2, namely 0.
            pair_num += temp_dict[key]*(temp_dict[key]-1)//2
        return pair_num

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        prior_str = self.countAndSay(n-1)
        sub_str_list = []       # Record the split string.
        i = 0
        while i < len(prior_str):
            """ Double pointers. """
            j = i + 1
            while j < len(prior_str) and prior_str[j] == prior_str[i]:
                j += 1
            sub_str_list += [prior_str[i: j]]
            i = j
        current_str = ''.join([str(len(sub_str))+sub_str[0] for sub_str in sub_str_list])
        return current_str

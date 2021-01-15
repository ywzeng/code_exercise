class Solution_better:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Non-recursion method. 
        Use the first string as the pattern to scan other strings.
        If not matched, modify the pattern to its [:-1] (namely remove the last character), and then rescan other strings.
        The final modified pattern is the longest common prefix.
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        
        result_str = strs[0]
        i = 1
        while i < len(strs):
            if strs[i][:len(result_str)] != result_str:
                result_str = result_str[:-1]
            else:
                i += 1
        return result_str


class Solution_stupid:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ Recursion method. """
        if not strs:
            return ''
        
        def recursion(str_list: list) -> str:
            is_common = True
            if not str_list[0] or not str_list[0][0]:
                return ''
            first_char = str_list[0][0]
            for i in range(1, len(str_list)):
                if not str_list[i] or str_list[i][0] != first_char:
                    is_common = False
                    break
            if is_common:
                temp_list = [temp_str[1:] for temp_str in str_list]
                return first_char + recursion(temp_list)
            else:
                return ''

        common_prefix = recursion(strs)
        return common_prefix

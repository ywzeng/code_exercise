class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
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

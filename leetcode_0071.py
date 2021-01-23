class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[-1] != '/':
            path += '/'
        stack = ['/']
        temp_path_start_index = 1
        while temp_path_start_index < len(path):
            temp_path_end_index = temp_path_start_index
            while path[temp_path_end_index] != '/' and temp_path_end_index < len(path)-1:
                temp_path_end_index += 1
            temp_path_str = path[temp_path_start_index: temp_path_end_index+1]
            temp_path_start_index = temp_path_end_index+1
            if temp_path_str == './':
                continue
            elif temp_path_str == '../':
                if len(stack) > 1:
                    stack.pop()
                continue
            elif temp_path_str == '/':
                continue
            else:
                stack += [temp_path_str]
        if len(stack) > 1 and stack[-1][-1] == '/':
            stack[-1] = stack[-1][:-1]
        return ''.join(stack)

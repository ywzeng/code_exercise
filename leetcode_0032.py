class Solution_stack_method:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0

        stack = [0]      # Store the indexes of the pushed parentheses.
        index_list = []     # Record the indexes of the matched parentheses.
        for i in range(1, len(s)):
            if s[i] == ')' and stack and s[stack[-1]] == '(':
                index_list += [stack.pop(), i]
            else:
                stack += [i]

        index_list.sort()
        longest_num = 0
        # Double pointers to find the consecutive indexes.
        i=0
        while i < len(index_list):
            j = i + 1
            while j < len(index_list) and index_list[j] - index_list[j-1] == 1:
                j += 1

            longest_num = max(longest_num, j-i)
            i = j
        return longest_num


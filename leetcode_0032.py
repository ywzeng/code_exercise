class Solution_DP:
    def longestValidParentheses(self, s: str) -> int:
        """ 
        The length of two matched parentheses is 2.
        DP
        dp[i] represents the longest valid parentheses number at s[i].
        If s[i] is '(', dp[i] = 0.
        If s[i] is ')' and s[i-1] is '(', dp[i] = dp[i-2] + 2.
        If s[i] is ')', s[i-1] is ')', and s[i-dp[i-1]-1] is '(', then dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2 if there are elements before (i-dp[i-1]-2), namely i-dp[i-1]-2 should >= 0, otherwise dp[i] = dp[i-1] + 2.
        """
        if len(s) < 2:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                # s[i-1] is ')' as well.
                elif i-dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2 if i - dp[i-1] >= 2 else dp[i-1] + 2
        return max(dp)


class Solution_Stack:
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


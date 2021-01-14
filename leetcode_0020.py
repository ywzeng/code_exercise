class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {'}': '{', ')': '(', ']': '['}
        stack = [s[0]]
        for c in s[1:]:
            if not stack or c not in pair_dict:
                stack += [c]
                continue
            if stack[-1] == pair_dict[c]:
                stack.pop()
            else:
                stack += [c]
        return False if stack else True

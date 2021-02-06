class Solution_Clever:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in list(s) if c.isalnum()]).lower()
        return s == s[::-1]

    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ Double pointers. """
        if not s:
            return True
        
        s = s.lower()
        left_p, right_p = 0, len(s)-1
        while left_p < right_p:
            if not s[left_p].isalnum():
                left_p += 1
                continue
            if not s[right_p].isalnum():
                right_p -= 1
                continue
            if s[left_p] != s[right_p] or left_p > right_p:
                return False
            left_p += 1
            right_p -= 1
        return True

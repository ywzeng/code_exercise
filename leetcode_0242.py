class Solution_HashMap:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t

class Solution_Sort:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = sorted(list(s)), sorted(list(t))
        return s == t

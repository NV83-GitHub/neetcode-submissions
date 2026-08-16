class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is None or t is None:
            return False
        return sorted(s) == sorted(t)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            result = haystack.index(needle)
            return result
        except Exception:
            return -1
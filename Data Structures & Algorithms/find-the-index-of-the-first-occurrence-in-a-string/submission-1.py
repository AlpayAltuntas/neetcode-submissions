class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        while l <= len(haystack) - len(needle):
            found = True
            for i in range(len(needle)):
                if haystack[l + i] != needle[i]:
                    found = False
                    break
            if found:
                return l
            l += 1
        return -1
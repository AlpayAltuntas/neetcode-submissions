class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, maxLen, curr, left = set(), 0, 0, 0
        while curr < len(s):
            if s[curr] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[curr])
                curr += 1
            maxLen = max(maxLen, len(seen))
        return maxLen

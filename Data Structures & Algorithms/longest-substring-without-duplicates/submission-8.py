class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        left = 0
        curr = 0

        while curr < len(s):
            if s[curr] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[curr])
                curr += 1

            max_length = max(max_length, len(seen))

        return max_length
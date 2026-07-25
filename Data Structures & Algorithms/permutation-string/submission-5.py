class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        freq1, freq2, matches = [0] * 26, [0] * 26, 0
        for i in range(n):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1
        if matches == 26:
            return True

        for char in range(n, m):
            idx = ord(s2[char]) - ord('a')
            if freq2[idx] == freq1[idx]: matches -= 1
            freq2[idx] += 1
            if freq2[idx] == freq1[idx]: matches += 1

            idx = ord(s2[char - n]) - ord('a')
            if freq2[idx] == freq1[idx]: matches -= 1
            freq2[idx] -= 1
            if freq2[idx] == freq1[idx]: matches += 1

            if matches == 26:
                return True

        return False
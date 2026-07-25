class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force
        res, charSetOfT, hashmap = "", set(t), {}
        for i in t:
            # set found to false for each item
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in range(len(s)):
            if s[i] not in charSetOfT:
                continue

            copyMap = hashmap.copy()
            curr = i
            currRes = ""
            matches = 0

            while curr < len(s):
                if s[curr] in charSetOfT and copyMap[s[curr]] > 0:
                    copyMap[s[curr]] -= 1
                    matches += 1

                currRes += s[curr]

                if matches == len(t):
                    if res == "" or len(currRes) < len(res):
                        res = currRes
                    break

                curr += 1

        return res

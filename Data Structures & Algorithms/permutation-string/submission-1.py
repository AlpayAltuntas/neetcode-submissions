class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1), len(s2)
        if n > m:
            return False

        frequencyS1,frequencyS2 = [0]*26, [0]*26
        for i in range(n):
            frequencyS1[ord(s1[i]) - ord('a')]+=1
            frequencyS2[ord(s2[i]) - ord('a')]+=1

        if frequencyS1 == frequencyS2:
            return True
        
        for i in range(n,m):
            frequencyS2[ord(s2[i]) - ord('a')]+=1
            frequencyS2[ord(s2[i-n]) - ord('a')]-=1
            if frequencyS1 == frequencyS2:
                return True
        return False
        

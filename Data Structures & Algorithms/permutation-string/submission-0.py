class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x,y = len(s1), len(s2)
        if x > y:
            return False
        
        s1 = sorted(s1)
        for i in range( y-x + 1):
            sorted_substring = sorted(s2[i:i+x])
            if sorted_substring == s1:
                return True
        return False
        
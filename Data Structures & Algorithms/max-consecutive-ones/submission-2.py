class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, maximum = 0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                maximum = max(maximum, curr)
                curr = 0
        return max(maximum, curr)
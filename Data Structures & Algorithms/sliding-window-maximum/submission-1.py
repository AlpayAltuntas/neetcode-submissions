class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        hashmap = {}
        res = []
        currMax = 0
        for i in range(0, len(nums) - k + 1):
            currList = nums[i:i+k]
            currMax = max(currList)
            res.append(currMax)
        return res
        
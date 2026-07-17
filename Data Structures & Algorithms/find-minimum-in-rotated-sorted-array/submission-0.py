class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        for i in nums:
            if i < minimum:
                minimum = i
        return minimum
        
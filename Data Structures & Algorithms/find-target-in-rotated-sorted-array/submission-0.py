class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # brute force
        for i,v in enumerate(nums):
            if v == target:
                return i
        return -1
        
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        heapq.heapify(nums)
        
        # Pop off the first half of the elements
        for _ in range(len(nums) // 2):
            heapq.heappop(nums)
            
        # The next smallest element is guaranteed to be the majority element
        return nums[0]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # with min heap
        h = nums
        heapq.heapify(h)
        res = []
        for i in range(len(nums)): 
            s = heapq.heappop(h)
            res.append(s)
        return res[len(res) - k]
        
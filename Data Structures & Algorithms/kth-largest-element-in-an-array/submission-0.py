class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # lets oush everything onto a max heap
        # then pop until we get the item k, return this
        h = [-x for x in nums]
        heapq.heapify(h)
        for i in range(k-1): heapq.heappop(h)
        res = heapq.heappop(h)
        return -res
        
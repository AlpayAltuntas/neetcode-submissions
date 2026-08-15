class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # lets have a minHeap
        ## compute distance of point, push to minHeap
        ## for k steps, pop from heap and onto a list
        heap = []
        for x,y in points:
            distance = x**2 + y**2
            heapq.heappush(heap, (distance, x, y))
        
        res = []
        while len(res) < k:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        return res
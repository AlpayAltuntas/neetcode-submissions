import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (negated values) — the lower half
        self.large = []  # min-heap — the upper half

    def addNum(self, num: int) -> None:
        # push to small (as a max-heap via negation)
        heapq.heappush(self.small, -num)
        # ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        # rebalance sizes so they differ by at most 1
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums) 
        myHeap = [(-count, num) for num, count in counts.items()]
        heapq.heapify(myHeap)
        most_frequent = heapq.heappop(myHeap)
        return most_frequent[1]
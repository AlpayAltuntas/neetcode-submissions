import bisect
class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        l, r = 0, len(self.arr)
        while l < r:
            m = l + (r - l) // 2
            if self.arr[m] < num:
                l = m + 1
            else:
                r = m
        self.arr.insert(l, num)

    def findMedian(self) -> float:
        arr_len = len(self.arr)
        if arr_len % 2 == 0:
            ml, mr = self.arr[arr_len // 2 - 1], self.arr[arr_len // 2]
            return (ml + mr) / 2
        else:
            return self.arr[arr_len // 2]


'''
easiest: array -> add to array and add using binary search
or even easier, add to array and sort

retrieval by binary search
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iterate from the back
        curr_max = arr[len(arr) - 1]
        i = len(arr) - 1
        while i >= 0:
            tmp = arr[i]
            arr[i] = curr_max
            if tmp > curr_max:
                curr_max = tmp
            i-=1
        arr[len(arr) - 1] = -1
        return arr
        
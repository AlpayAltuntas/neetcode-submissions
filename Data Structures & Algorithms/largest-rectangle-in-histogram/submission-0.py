class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maximum = 0
        for i in range(len(heights)) :
            curr_item = heights[i]
            j = i + 1
            maximum = curr_item if curr_item > maximum else maximum
            item_min = curr_item
            while j < len(heights):
                item_min = min(item_min, heights[j])
                rectangle = (j - i + 1) * item_min
                maximum = rectangle if rectangle > maximum else maximum
                j+=1
        return maximum 
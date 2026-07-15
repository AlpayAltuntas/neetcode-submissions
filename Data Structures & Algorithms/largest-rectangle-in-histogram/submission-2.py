class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n,maxArea,stack = len(heights), 0, []
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx,ht = stack.pop()
                maxArea = max(maxArea, ht * (i-idx) )
                start = idx
            stack.append((start,h))
        
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        used = [False] * len(nums)

        def dfs():
            # base case
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            # Go through items
            for i in range(len(nums)):
                if used[i]: continue
                used[i] = True
                subset.append(nums[i])
                dfs()
                subset.pop()
                used[i] = False

        dfs()
        return res
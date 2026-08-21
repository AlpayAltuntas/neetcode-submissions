class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # clearly dfs
        res = []

        def dfs(start, amount_left, curr):
            nonlocal res
            if amount_left == 0:
                res.append(curr[:])                  # append a copy
                return
            if amount_left < 0:
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i, amount_left - nums[i], curr)  # i, not i+1 → reuse allowed
                curr.pop()                           # backtrack (no argument)

        dfs(0, target, [])
        return res
        
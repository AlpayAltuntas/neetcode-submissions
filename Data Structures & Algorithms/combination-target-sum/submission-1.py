class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start, amount_left, curr):
            if amount_left == 0:
                res.append(curr[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > amount_left:   # sorted → rest are too big, stop
                    break
                curr.append(nums[i])
                dfs(i, amount_left - nums[i], curr)
                curr.pop()

        dfs(0, target, [])
        return res
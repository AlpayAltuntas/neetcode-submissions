class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, amount_left, curr):
            if amount_left == 0:
                res.append(curr[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > amount_left:   # sorted → rest are too big, stop
                    break
                curr.append(candidates[i])
                dfs(i + 1, amount_left - candidates[i], curr)
                curr.pop()

        dfs(0, target, [])
        return res
        
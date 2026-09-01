class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, open_count, close_count):
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return
            if open_count < n:                      # can still open
                curr.append('(')
                backtrack(curr, open_count + 1, close_count)
                curr.pop()
            if close_count < open_count:            # can close only if there's an unmatched (
                curr.append(')')
                backtrack(curr, open_count, close_count + 1)
                curr.pop()
        backtrack([], 0, 0)
        return res
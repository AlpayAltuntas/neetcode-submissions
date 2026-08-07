class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # go through the array
        ## have a curr_sequence array
        res, curr, sequence = 0,0,False
        for i in nums:
            if i != 1: 
                sequence = False
                res = max(curr, res)
                curr = 0
            else:
                sequence = True
                curr += 1
        return max(res,curr)
            

        
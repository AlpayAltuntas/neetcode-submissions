class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l,r,res,n1,n2 = [],[],[],set(nums1), set(nums2)
        for i in n1:
            if (i in n1) and (i not in n2):
                l.append(i)
        for i in n2:
            if (i not in n1) and (i in n2):
                r.append(i)
        
        res.append(l)
        res.append(r)
        return res

        
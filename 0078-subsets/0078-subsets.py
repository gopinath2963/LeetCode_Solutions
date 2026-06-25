class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = self.subsets(nums[:-1])
        
        for i in range(len(res)):

             res.append(res[i] + [nums[-1]])
        return res

        
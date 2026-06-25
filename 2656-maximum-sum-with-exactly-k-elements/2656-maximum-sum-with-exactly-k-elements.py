class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = nums[-1]
        f=0
        print(l)
        for i in range(k):
            f = f + l
            l = l + 1
        return f 

        
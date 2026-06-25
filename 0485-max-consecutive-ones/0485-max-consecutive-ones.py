class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        c1=[]
        for i in range(len(nums)):
            if nums[i] == 1:
                c=c+1
            else:
                c1.append(c)
                c=0
            c1.append(c)
        return max(c1)

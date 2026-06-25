class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        j=0
        res=[]
        for i in range(n,len(nums)):
            res.append(nums[j])
            res.append(nums[i])
            j+=1
        return res
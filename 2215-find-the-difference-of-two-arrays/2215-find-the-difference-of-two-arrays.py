class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s1=set(nums1)
        s2=set(nums2)
        s3=[]

        o= s1 - s2
        b= s2 - s1
        

        s3.append(list(o))
        s3.append(list(b))       

        return s3

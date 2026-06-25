class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        s1=set(nums1)
        s2=set(nums2)
        n1=s1.intersection(s2)
        if not n1:
            return -1
        else:
            li=list(n1)
            #print(li)
            print(li.sort())
            l2=li[0]
        return l2
        





        
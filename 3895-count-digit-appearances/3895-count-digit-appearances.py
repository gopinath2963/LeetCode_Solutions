class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        l=[]
        c=0
        for i in nums:
            b=str(i)
            for j in range(len(b)):
                if int(b[j])==digit:
                    c=c+1
        return c
      

            
        
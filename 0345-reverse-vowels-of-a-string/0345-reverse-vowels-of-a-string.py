class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        i=0
        j=len(s)-1
        vow = "AEIOUaeiou"
        a = list(s)

        while(i<j):
            if a[i] in vow and a[j] in vow:
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
            elif a[i] in vow and a[j] not in vow:
                j-=1
            elif a[i] not in vow and a[j] in vow:
                i+=1
            else:
                i+=1
                j-=1
        

        return "".join(a)
                

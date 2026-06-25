class Solution(object):
    def sortVowels(self, s):
        v=[]
        f=""

        for i in s:
            if i in "AEIOUaeiou":
                v.append(i)

        a = sorted(v)
        j=0
        for i in s:
            if i in "AEIOUaeiou":
                f = f+a[j]
                j=j+1
            else:
                f = f+i
        return f

       
        
class Solution(object):
    def maxNumberOfBalloons(self, text):
        freq={}
        s ="balloon"
        c=0
        s1="ban"
        s2="lo"
        for i in text:
            freq[i]=freq.get(i,0)+1
        c1= freq.get("b")
        c2 = freq.get("l")
        c3=[ freq.get(s1[i],0) for i in range(len(s1))]
        c4 =[freq.get(s2[i],0)//2 for i in range(len(s2))]

        m = c3 + c4
        m1 = min(m)
        print(m1)
        if m1 == 0:
            return 0
        return m1

        
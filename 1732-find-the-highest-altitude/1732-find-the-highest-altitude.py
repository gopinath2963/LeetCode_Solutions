class Solution(object):
    def largestAltitude(self, gain):
        maxi=0
        sums=0
        for ele in gain:
            sums+=ele
            if maxi<sums:
                maxi=sums
        print(maxi)
        return maxi
            
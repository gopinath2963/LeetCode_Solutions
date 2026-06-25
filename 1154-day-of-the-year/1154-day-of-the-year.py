class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        d = date.split("-")
        dd = int(d[-1])
        mm = int(d[1])
        yr = int(d[0])
        a = 0

        if (yr%4 == 0 and yr%100 != 0) or yr%400 == 0:
            f = 29
        else:
            f = 28


        calendar_months = {
            1: 31,          # January
            2: f,    # February (Common / Leap year)
            3: 31,          # March
            4: 30,          # April
            5: 31,          # May
            6: 30,          # June
            7: 31,          # July
            8: 31,          # August
            9: 30,          # September
            10: 31,         # October
            11: 30,         # November
            12: 31          # December
        }


        
        for i in range(1,mm):
            a += calendar_months[i]

        return a+dd


        
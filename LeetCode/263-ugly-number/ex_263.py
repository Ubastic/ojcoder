class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = num
        if res == 0:
            return False
        if res == 1:
            return True
        while (res % 2 == 0):
            res /= 2
        while (res % 3 == 0):
            res /= 3
        while (res % 5 == 0):
            res /= 5
        return res == 1
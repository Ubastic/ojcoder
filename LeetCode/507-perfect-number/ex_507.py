class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:    return False
        count = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                count += i + num / i
            i += 1
        return count == num
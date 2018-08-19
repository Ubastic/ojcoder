class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        zeros = 0
        while num:
                zeros += num / 5
                num /= 5
        return zeros

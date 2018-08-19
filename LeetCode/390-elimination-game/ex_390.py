class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        reverse = False
        head = 1
        step = 1
        while n > 1:
            if not reverse or n % 2:
                head += step
            n /= 2
            step *= 2
            reverse = not reverse
        return head
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start <= end:
            mid = start + (end - start) / 2
            res = guess(mid)
            if res == 0:
                return mid
            if res == -1:
                end = mid - 1
            else:
                start = mid + 1
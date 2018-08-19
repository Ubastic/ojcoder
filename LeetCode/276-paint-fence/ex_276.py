class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:  return 0
        if n == 1:  return k
        same_color, diff_color = k, k * (k - 1)
        for i in xrange(3, n + 1):
            same_color, diff_color = diff_color, (same_color + diff_color) * (k - 1)
        return same_color + diff_color
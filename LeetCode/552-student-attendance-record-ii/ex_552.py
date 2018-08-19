class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1000000007
        a0l0 = 1
        a0l1 = a0l2 = a1l0 = a1l1 = a1l2 = 0
        for i in range(n+1):
            a0l0_ = (a0l0 + a0l1 + a0l2) % m
            a0l2 = a0l1
            a0l1 = a0l0
            a0l0 = a0l0_
            a1l0_ = (a0l0_ + a1l0 + a1l1 + a1l2) % m
            a1l2 = a1l1
            a1l1 = a1l0
            a1l0 = a1l0_
        return a1l0

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        diff = sys.maxsize
        count = 0
        n = 0
        for i in xrange(1, len(A)):
            if diff != A[i] - A[i-1]:
                diff = A[i] - A[i-1]
                count += sum(xrange(n + 1))
                n = 0
            else:
                n += 1
        if n > 0:
            count += sum(xrange(n + 1))
        return count
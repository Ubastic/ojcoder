class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for start, end, val in updates:
            res[start] += val
            if end + 1 < length:
                res[end + 1] -= val
        for i in xrange(1, length):
            res[i] += res[i-1]
        return res
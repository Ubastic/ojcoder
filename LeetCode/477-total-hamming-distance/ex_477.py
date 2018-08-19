class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        res = 0
        for i in xrange(32):
            cnt = 0
            for n in nums:
                cnt += (n >> i) & 1
            res += cnt * (length - cnt)
        return res
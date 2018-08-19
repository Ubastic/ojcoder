class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = (n + 1) * n / 2
        for i in nums:
            res -= i
        return res
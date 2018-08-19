class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_n = min(nums)
        res = 0
        for n in nums:
            res += n - min_n
        return res
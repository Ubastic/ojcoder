class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        table = {}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s == k: 
                res = max(res, i + 1)
            elif s - k in table:
                res = max(res, i - table[s - k])
            if s not in table:
                table[s] = i
        return res
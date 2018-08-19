class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        table = {}
        res = s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s == 0:
                res = max(res, i + 1)
            elif s in table:
                res = max(res, i - table[s])
            else:
                table[s] = i
        return res
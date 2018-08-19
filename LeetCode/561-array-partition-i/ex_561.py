class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:    return 0
        res = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            res += min(nums[i], nums[i+1])
        return res
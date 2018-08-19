class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
            return False
        memo = {}
        return self.helper(memo, range(1, maxChoosableInteger + 1), desiredTotal)
        
    def helper(self, memo, nums, desiredTotal):
        key = str(nums)
        if key in memo:
            return memo[key]
        if nums[-1] >= desiredTotal:
            return True
        for i in range(len(nums)):
            if not self.helper(memo, nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                memo[key] = True
                return True
        memo[key] = False
        return False
            
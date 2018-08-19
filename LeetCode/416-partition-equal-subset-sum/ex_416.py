class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:   return False
        target = sum(nums) / 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for t in range(target, n-1, -1):
                dp[t] |= dp[t-n]
        return dp[-1]
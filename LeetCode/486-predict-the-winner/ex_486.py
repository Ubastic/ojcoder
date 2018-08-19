class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [[-1] * len(nums) for _ in range(len(nums))]
        self.helper(nums, dp, 0, len(nums) - 1)
        return 2 * dp[0][-1] >= sum(nums)
        
    def helper(self, nums, dp, i, j):
        if i > j:   return 0
        if dp[i][j] != -1:  return dp[i][j]
        s = self.helper(nums, dp, i+1, j-1)
        a = nums[i] + min(s, self.helper(nums, dp, i+2, j))
        b = nums[j] + min(s, self.helper(nums, dp, i, j-2))
        dp[i][j] = max(a, b)
        return dp[i][j]
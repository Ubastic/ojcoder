class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = range(1, N + 1)
        return self.count(nums, N)
        
    def count(self, nums, n):
        if n <= 0:  return 1
        cnt = 0
        for i in range(n):
            if nums[i] % n == 0 or n % nums[i] == 0:
                nums[i], nums[n-1] = nums[n-1], nums[i]
                cnt += self.count(nums, n-1)
                nums[i], nums[n-1] = nums[n-1], nums[i]
        return cnt
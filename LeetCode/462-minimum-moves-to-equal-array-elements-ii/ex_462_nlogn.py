class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort()
        mid = len(nums) / 2
        median = nums[mid] if len(nums) % 2 else (nums[mid] + nums[mid - 1]) / 2
        for n in nums:
            count += abs(n - median)
        return count
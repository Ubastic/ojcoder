class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums) + 1
        curr_sum = 0
        i = j = 0
        while i < len(nums):
            curr_sum += nums[i]
            while curr_sum >= s:
                res = min(res, i - j + 1)
                curr_sum -= nums[j]
                j += 1
            i += 1
            
        return 0 if res == len(nums) + 1 else res
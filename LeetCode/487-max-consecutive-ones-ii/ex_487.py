class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        left = right = 0
        for n in nums:
            right += 1
            if n == 0:
                left = right
                right = 0
            max_count = max(max_count, left + right)
        return max_count
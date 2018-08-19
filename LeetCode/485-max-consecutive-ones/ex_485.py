class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = count = 0
        for n in nums:
            if n == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
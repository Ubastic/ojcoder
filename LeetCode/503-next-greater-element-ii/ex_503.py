class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [-1] * length
        stack = []
        for i in xrange(length * 2):
            n = nums[i % length]
            while stack and nums[stack[-1]] < n:
                res[stack[-1]] = n
                stack.pop()
            if i < length:  stack.append(i)
        return res
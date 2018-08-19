class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def transform(x):
            return a * x * x + b * x + c
        if a == 0:
            res = map(transform, nums)
            return res if b > 0 else res[::-1]
        line = -1.0 * b / (2 * a)
        i = j = 0
        while nums[j] < line:
            i = j
            j += 1
        res = []
        while i >= 0 and j < len(nums):
            if abs(nums[i] - line) < abs(nums[j] - line):
                res.append(transform(nums[i]))
                i -= 1
            else:
                res.append(transform(nums[j]))
                j += 1
        while i >= 0:
            res.append(transform(nums[i]))
            i -= 1
        while j < len(nums):
            res.append(transform(nums[j]))
            j += 1
        return res if a > 0 else res[::-1]
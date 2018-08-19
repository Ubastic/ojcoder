class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or r * c > len(nums) * len(nums[0]):   return nums
        vals = []
        for row in nums:
            vals.extend(row)
        i = 0
        row = 0
        res = []
        while row < r:
            res.append(vals[i:i+c])
            i += c
            row += 1
        return res
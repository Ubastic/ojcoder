class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        num = 0
        for n in nums:
            num ^= n
        return num

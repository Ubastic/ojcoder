class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:    return 0
        table = {}
        res = 0
        for n in nums:
            if n not in table:
                temp = 0
                left = right = 0
                if n - 1 in table:
                    left += table[n - 1]
                if n + 1 in table:
                    right += table[n + 1]
                temp = 1 + left + right
                table[n] = temp
                res = max(res, temp)
                table[n - left] = temp
                table[n + right] = temp
        return res
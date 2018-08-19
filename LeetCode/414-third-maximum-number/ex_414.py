class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:    return 0
        first = second = third = float('-inf')
        for n in nums:
            if n > first:
                third, second, first = second, first, n
            elif n < first:
                if n > second:
                    third, second = second, n
                elif n < second:
                    if n > third:
                        third = n
        if third == float('-inf'):
            return first
        return third
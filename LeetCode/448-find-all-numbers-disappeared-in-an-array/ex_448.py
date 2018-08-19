class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set([x + 1 for x in xrange(len(nums))]) - set(nums))
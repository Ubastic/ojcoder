class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mset = set()
        res = []
        for n in nums:
            if n in mset:
                res.append(n)
            else:
                mset.add(n)
        return res
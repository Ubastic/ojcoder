class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = res = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefix_set = set()
            for n in nums:
                prefix_set.add(n & mask)
            candidate = res | 1 << i
            for prefix in prefix_set:
                # if A ^ B = candidate
                # then we also have A ^ candidate = B or B ^ candidate = A
                if prefix ^ candidate in prefix_set:
                    res = candidate
                    break
        return res
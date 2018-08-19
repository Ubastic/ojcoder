class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k < 0:   return 0
        counter = collections.Counter(nums)
        pairs = set()
        for n in nums:
            counter[n] -= 1
            if counter[n+k]:
                pairs.add((n, n+k))
            counter[n] += 1
        return len(pairs)
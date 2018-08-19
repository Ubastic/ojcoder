class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return
        s = [0] * len(nums)
        for i in range(len(nums)):
            s[i] = s[i-1] + nums[i]
        count = 0
        counter = collections.Counter(s)
        for i in range(len(s)):
            count += counter[s[i] + k - nums[i]]
            if counter[s[i]] > 0:
                counter[s[i]] -= 1
        return count
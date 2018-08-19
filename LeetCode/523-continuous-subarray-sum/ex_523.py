class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:   return False
        seen = set([nums[0], 0])
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] == 0:    return True
            elif k == 0: continue
            else:
                s = (s + nums[i]) % k
                if s in seen:   return True
                seen.add(s)
        return False
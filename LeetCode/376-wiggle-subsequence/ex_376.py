class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:    return len(nums)
        prev_diff = nums[1] - nums[0]
        if prev_diff != 0:
            longest = 2
        else:
            longest = 1
        for i in range(2, len(nums)):
            curr_diff = (nums[i] - nums[i-1])
            if (curr_diff > 0 and prev_diff <= 0) or (curr_diff < 0 and prev_diff >= 0):
                longest += 1
                prev_diff = curr_diff
        return longest
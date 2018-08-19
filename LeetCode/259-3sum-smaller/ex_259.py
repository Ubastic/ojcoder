class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in xrange(len(nums) - 2):
            t = target - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < t:   
                    count += k - j    
                    j += 1
                else:
                    k -= 1
        return count
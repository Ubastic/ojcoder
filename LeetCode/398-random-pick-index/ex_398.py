class Solution(object):
    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 1
        res = None
        for i, n in enumerate(self.nums):
            if n == target:
                if random.randint(1, count) == 1:
                    res = i
                count += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
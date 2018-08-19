class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or sum(nums) % 4:   return False
        tar = sum(nums) / 4
        sides = [0, 0, 0, 0]
        nums.sort(reverse=True)
        return self.dfs(sides, nums, 0, len(nums), tar)
    
    def dfs(self, sides, nums, i, j, target):
        if i == j:  return all(x == target for x in sides)
        v = nums[i]
        for k in range(4):
            if sides[k] + v <= target:
                sides[k] += v
                if self.dfs(sides, nums, i+1, j, target):   return True
                sides[k] -= v
        return False
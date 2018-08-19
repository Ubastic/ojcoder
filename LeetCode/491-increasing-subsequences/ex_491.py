class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [], 0)
        return res
        
    def dfs(self, nums, res, partial, i):
        if len(partial) > 1:
            res.append(partial)
        visited = set()
        for j in range(i, len(nums)):
            if not partial or nums[j] >= partial[-1]:
                if nums[j] not in visited:
                    visited.add(nums[j])
                    self.dfs(nums, res, partial + [nums[j]], j + 1)
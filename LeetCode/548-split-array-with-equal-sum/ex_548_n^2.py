class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 7:   return False
        s = [nums[0]]
        for i in range(1, n):
            s.append(s[-1] + nums[i])
        
        for j in range(3, n - 3):
            seen = set()
            for i in range(1, j - 1):
                if s[i-1] == s[j-1] - s[i]:
                    seen.add(s[i-1])
            for k in range(j + 2, n - 1):
                if s[k-1] - s[j] == s[n-1] - s[k] and s[n-1] - s[k] in seen:
                    return True
        return False
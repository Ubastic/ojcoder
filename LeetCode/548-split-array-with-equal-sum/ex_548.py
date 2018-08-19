class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 5:   return False
        n = len(nums)
        s = [0]
        for i in range(n):
            s.append(s[-1] + nums[i])
        
        for i in range(n - 5):
            if i > 0 and s[i] == s[i-1]: continue
            a = s[i]
            for j in range(i + 2, n - 3):
                b = s[j] - s[i+1]
                if a != b:  continue
                for k in range(j + 2, n - 1):
                    c = s[k] - s[j+1]
                    if a != c:  continue
                    d = s[-1] - s[k+1]
                    if a == d == c:
                        return True
        return False
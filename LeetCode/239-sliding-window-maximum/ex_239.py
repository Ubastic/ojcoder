from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:    return []
        rtn = []
        dq = deque()
        for i in range(len(nums)):
            if dq and dq[0] < i-(k-1):
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i > k - 2:
                rtn.append(nums[dq[0]])
        return rtn
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        for i in nums:
            n = [i, i]
            while stack and stack[-1][1] <= i:
                n[0] = min(stack[-1][0], n[0])
                stack.pop()
            if stack and stack[-1][1] > i and stack[-1][0] < i:
                return True
            stack.append(n)
        return False
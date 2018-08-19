class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if not findNums:    return []
        table = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                table[stack[-1]] = n
                stack.pop()
            stack.append(n)
        res = []
        for n in findNums:
            if n in table:
                res.append(table[n])
            else:
                res.append(-1)
        return res
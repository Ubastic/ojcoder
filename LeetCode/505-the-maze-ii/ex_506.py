class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        lst = []
        for i, n in enumerate(nums):
            lst.append((n, i))
        lst.sort(reverse=True)
        table = {1:'Gold Medal', 2:'Silver Medal' ,3:'Bronze Medal'}
        for i in range(0, len(nums)):
            num = lst[i][0]
            index = lst[i][1]
            if i + 1 <= 3:
                nums[index] = table[i + 1]
            else:
                nums[index] = str(i + 1)
        return nums
        
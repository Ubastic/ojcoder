class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        arr = []
        for t in timePoints:
           h, m = map(int, t.split(':'))
           arr.append(h * 60 + m)
        arr.sort()
        arr.append(arr[0] + 1440)
        res = 1440
        for i in range(1, len(arr)):
            res = min(res, arr[i] - arr[i-1])
        return res
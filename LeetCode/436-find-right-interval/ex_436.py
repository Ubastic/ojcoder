# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        res = []
        arr = sorted((v.start, i) for i, v in enumerate(intervals))
        for i in intervals:
            '''
            Due to sorting order, we must use tuple for bisect_left function, a tuple with single element is also ok
            tuple with single element: (1,)
            see sorted list with tuples and int:
            [1, (0, 1), (0, 2), (1,), (1, 1), (1, 3), (1, 6), (1, 10000), (2, 1)]
            bisect uses binary search, which makes it O(logn)
            '''
            right = bisect.bisect_left(arr, (i.end, -1))

            res.append(arr[right][1] if right < len(arr) else -1)
        return res
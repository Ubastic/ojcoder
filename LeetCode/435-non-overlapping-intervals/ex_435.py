# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x: x.end)
        count = 0
        end = float('-inf')
        for i in intervals:
            if i.start >= end:
                end = i.end
                count += 1
        return len(intervals) - count
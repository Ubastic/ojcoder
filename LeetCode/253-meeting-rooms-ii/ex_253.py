# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:   return 0
        start = sorted(x.start for x in intervals)
        end = sorted(x.end for x in intervals)
        i = 0
        available = rooms = 0
        for s in start:
            while end[i] <= s:
                available += 1
                i += 1
            if not available:
                rooms += 1
            else:
                available -= 1
                
        return rooms
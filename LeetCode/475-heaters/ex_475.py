class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = -1
        heaters.sort()
        for h in houses:
            i = bisect.bisect_left(heaters, h)
            left_dist = h - heaters[i - 1] if i > 0 else sys.maxsize
            right_dist = heaters[i] - h if i < len(heaters) else sys.maxsize
            res = max(res, min(left_dist, right_dist))
        return res
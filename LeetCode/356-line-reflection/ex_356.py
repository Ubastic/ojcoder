class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        max_x = float('-inf')
        min_x = float('inf')
        points_set = set()
        for p in points:
            max_x = max(p[0], max_x)
            min_x = min(p[0], min_x)
            points_set.add(tuple(p))
        s = max_x + min_x
        for p in points:
            r = (s - p[0], p[1])
            if r not in points_set:
                return False
        return True
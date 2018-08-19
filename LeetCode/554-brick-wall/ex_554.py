class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        res = n = len(wall)
        counter = {}
        for row in wall:
            i = 0
            for j in range(len(row) - 1):
                i += row[j]
                if i not in counter:
                    counter[i] = 0
                counter[i] += 1
        for v in counter.values():
            res = min(res, n - v)
        return res
        
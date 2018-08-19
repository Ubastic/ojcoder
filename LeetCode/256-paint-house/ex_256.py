class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:    return 0
        prev = costs[0][:]
        curr = [0] * 3
        for i in xrange(len(costs) - 1):
            curr[0] = min(prev[1], prev[2]) + costs[i+1][0]
            curr[1] = min(prev[0], prev[2]) + costs[i+1][1]
            curr[2] = min(prev[1], prev[0]) + costs[i+1][2]
            prev[:] = curr[:]
        return min(prev)
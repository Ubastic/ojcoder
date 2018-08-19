class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        pairs = []
        for i in range(len(Profits)):
            pairs.append((Capital[i], -Profits[i]))
        pairs.sort()
        heap = []
        cap = W
        i = 0
        while k > 0:
            while i < len(pairs) and pairs[i][0] <= cap:
                heapq.heappush(heap, (pairs[i][1], pairs[i][0]))
                i += 1
            if len(heap) == 0:  break
            project = heapq.heappop(heap)
            cap -= project[0]
            k -= 1
        return cap
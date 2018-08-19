class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_so_far = sys.maxsize
        max_profit = 0
        for i in prices:
            max_profit = max(max_profit, i - min_so_far)
            min_so_far = min(min_so_far, i)
        return max_profit
        